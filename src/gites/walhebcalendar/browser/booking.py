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
        elif requestData._bookingType in ['available']:
            self._removeBookings(requestData)
        session.add(notf)
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
                bookings.append(wsBooking)
            else:
                wsBooking._endDate = booking.book_date
            lastKey = (booking.book_date + timedelta(days=1), booking.book_booking_type,
                       booking.book_cgt_id)

        response._bookings = bookings
        return response

    @validate
    def getNotificationsRequest(self, requestData, response):
        notfs = []
        minNotificationId = requestData._minNotificationId
        maxNotificationId = requestData._maxNotificationId
        query = self.session.query(Notification)
        query = query.filter(Notification.notf_id >= minNotificationId)
        if maxNotificationId:
            query = query.filter(Notification.notf_id <= maxNotificationId)
        query = query.order_by(Notification.notf_id)
        for notif in query.all():
            wsNotf = response.new_notifications()
            wsNotf._cgtId = notif.notf_cgt_id
            wsNotf._notificationId = notif.notf_id
            wsNotf._startDate = notif.notf_start_date
            wsNotf._endDate = notif.notf_end_date
            wsNotf._bookingType = notif.notf_booking_type
            notfs.append(wsNotf)
        response._notifications = notfs
        return response

    @validate
    def cancelBookingRequest(self, requestData, response):
        requestData._bookingType = 'available'
        return self.addBookingRequest(requestData, response)

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
        for booking in self._getBookings(booking._cgtId,
                                         booking._startDate,
                                         booking._endDate):
            self.session.delete(booking)

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
        elif isinstance(cgtId, (str, unicode)):
            query = query.filter(Booking.book_cgt_id == cgtId)
        query = query.filter(Booking.book_date.between(startDate, endDate))
        query = query.order_by(Booking.book_cgt_id, Booking.book_date)
        return query
