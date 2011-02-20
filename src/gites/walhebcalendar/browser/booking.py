# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from datetime import datetime
from datetime import time
from datetime import timedelta
from dateutil.rrule import DAILY, rrule
from zope.component import getUtility
from affinitic.db.interfaces import IDatabase
from walhebcalendar.db.booking import Booking
from walhebcalendar.db.notification import Notification
from gites.walhebcalendar.browser.utils import validate, getUsername
from plone.memoize.instance import memoize


class SOAPBookingManagement(object):

    @validate
    def addBookingRequest(self, requestData, response):
        session = self.session
        notf = self._addNotification(requestData)
        if requestData._bookingType in ['booked', 'unavailable']:
            bookings = self._addBookings(requestData, notf)
            notf.createdBookings = list(bookings)
            session.add(notf)
        elif requestData._bookingType in ['available']:
            self._removeBookings(requestData)
        session.flush()
        response._notificationId = notf.notf_id
        return response

    @validate
    def getBookingsRequest(self, requestData, response):
        bookings = []
        lastKey = None
        for booking in self._getBookings(requestData._cgtId, requestData._minDate,
                                         requestData._maxDate):
            newKey = (booking.book_date, booking.book_booking_type, booking.book_cgt_id)
            if lastKey is None or lastKey != newKey:
                wsBooking = response.new_bookings()
                wsBooking._startDate = booking.book_date
                wsBooking._endDate = booking.book_date
                wsBooking._cgtId = booking.book_cgt_id
                wsBooking._bookingType = booking.book_booking_type
                lastKey = (booking.book_date + timedelta(days=1), booking.book_booking_type,
                           booking.book_cgt_id)
                bookings.append(wsBooking)
            else:
                wsBooking._endDate = booking.book_date
        response._bookings = bookings
        return response

    @property
    @memoize
    def session(self):
        db = getUtility(IDatabase, 'pg')
        return db.session

    def _addNotification(self, booking):
        notf = Notification()
        notf.notf_cgt_id = booking._cgtId
        notf.notf_user_id = getUsername()
        notf.notf_start_date = booking._startDate
        notf.notf_end_date = booking._endDate
        notf.notf_booking_type = booking._bookingType
        return notf

    def _addBookings(self, booking, notification):
        dates = rrule(DAILY, dtstart=booking._startDate, until=booking._endDate)
        currentBookings = self._getBookingsGroupedByDays(booking._cgtId, booking._startDate, booking._endDate)
        for nDate in dates:
            book = Booking()
            book.book_cgt_id = booking._cgtId
            book.book_date = nDate
            previousBook = currentBookings.get(nDate)
            if previousBook is not None:
                if previousBook.book_booking_type != booking._bookingType:
                    previousBook.update_notification = notification
                    previousBook.book_booking_type = booking._bookingType
            else:
                book.book_booking_type = booking._bookingType
                yield book

    def _removeBookings(self, booking):
        pass

    def _getBookingsGroupedByDays(self, cgtId, startDate, endDate):
        bookings = {}
        for booking in self._getBookings(cgtId, startDate, endDate):
            bookKey = datetime.combine(booking.book_date, time())
            bookings[bookKey] = booking
        return bookings

    def _getBookings(self, cgtId, startDate, endDate):
        query = self.session.query(Booking)
        if isinstance(cgtId, (list, set)) and len(cgtId) > 0:
            query = query.filter(Booking.book_cgt_id.in_(cgtId))
        elif isinstance(cgtId, (int, float)):
            query = query.filter(Booking.book_cgt_id == cgtId)
        query = query.filter(Booking.book_date.between(startDate, endDate))
        query = query.order_by(Booking.book_cgt_id, Booking.book_date)
        return query
