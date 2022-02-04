# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
import datetime
import os

from ZSI.auth import AUTH
from tempfile import mkstemp
from gites.walhebcalendar.zsi.booking_client import (bookingLocator, addBookingRequest,
                                                     getBookingsRequest, getNotificationsRequest,
                                                     cancelBookingRequest)


def get_calendar_client_url():
    return os.getenv(
        "CALENDAR_CLIENT_URL_6011",
        "http://localhost:6011/calendar"
    )


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


def main():
    from datetime import date
    client = CalendarClient(get_calendar_client_url(), login='admin',
                            passwd='admin')
    startDate = date(2035, 1, 1)
    endDate = date(2035, 1, 4)
    print client.getBookings(startDate, endDate)
    startDate = date(2016, 2, 16)
    endDate = date(2016, 2, 19)
    client.addBooking('GRLX4354', startDate, endDate, 'unavailable')
