# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
import datetime
from ZSI.auth import AUTH
from tempfile import mkstemp
from gites.walhebcalendar.zsi.booking_client import bookingLocator, addBookingRequest


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


        kwargs = dict(url=self.url, tracefile=self.trace,
                      auth=(AUTH.httpbasic, login, passwd))

        self.port = self.service(**kwargs)

    @property
    def service(self):
        return bookingLocator().getbookingSOAP

    def addBooking(self, cgtId, startDate, endDate, bookingType='booked'):
        bookingRequest = addBookingRequest()
        bookingRequest._cgtId = cgtId
        bookingRequest._startDate = startDate
        bookingRequest._endDate = endDate
        response = self.port.addBooking(bookingRequest)
        return response._notificationId

    def close(self):
        self.trace.close()
