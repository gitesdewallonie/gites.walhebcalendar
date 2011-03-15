# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
import datetime
from ZSI.auth import AUTH
from tempfile import mkstemp
from gites.walhebcalendar.zsi.booking_client import (bookingLocator, addBookingRequest,
                                                     getBookingsRequest, getNotificationsRequest,
                                                     cancelBookingRequest)


class CalendarClient(object):
    """
    Basic client
    """

    logFilename = None
    checkProxy = True

    def __init__(self, url, proxy=None, logToFile=False, login='user1',
                 passwd='secret'):
        self.url = url
        d = datetime.date.today()
        if logToFile:
            self.trace = open('/var/log/xml/%s-%s.log' % (self.logFilename,
                                                      d.strftime("%d-%m-%Y")),
                              'a')
        elif self.logFilename:
            self.fp, self.logFilename = mkstemp(dir='/tmp',
                                                prefix=self.logFilename)
            self.trace = open(self.logFilename, 'a')
        else:
            self.trace = None

        kwargs = dict(url=self.url, tracefile=self.trace)
        if login and passwd:
            kwargs['auth'] = (AUTH.httpbasic, login, passwd)

        self.port = self.service(**kwargs)

    @property
    def service(self):
        return bookingLocator().getbookingSOAP

    def addBooking(self, cgtId, startDate, endDate, bookingType='booked'):
        """
        Add a booking
        """
        bookingRequest = addBookingRequest()
        bookingRequest._cgtId = cgtId
        bookingRequest._startDate = startDate
        bookingRequest._endDate = endDate
        bookingRequest._bookingType = bookingType
        response = self.port.addBooking(bookingRequest)
        return response._notificationId

    def getBookings(self, startDate, endDate, cgtIds=[]):
        """
        Get available bookings
        """
        if not isinstance(cgtIds, (list, set)):
            cgtIds = [cgtIds]
        bookingRequest = getBookingsRequest()
        bookingRequest._minDate = startDate
        bookingRequest._maxDate = endDate
        bookingRequest._cgtId = cgtIds
        response = self.port.getBookings(bookingRequest)
        return response._bookings

    def getNotifications(self, minNotificationId, maxNotificationId=None):
        """
        Get available notifications
        """
        notifRequest = getNotificationsRequest()
        notifRequest._minNotificationId = minNotificationId
        notifRequest._maxNotificationId = maxNotificationId
        response = self.port.getNotifications(notifRequest)
        return response._notifications

    def cancelBooking(self, cgtId, startDate, endDate):
        """
        Cancel a booking
        """
        cancelRequest = cancelBookingRequest()
        cancelRequest._cgtId = cgtId
        cancelRequest._startDate = startDate
        cancelRequest._endDate = endDate
        response = self.port.cancelBooking(cancelRequest)
        return response._notificationId

    def close(self):
        self.trace.close()
