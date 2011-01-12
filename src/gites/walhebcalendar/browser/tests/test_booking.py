# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from datetime import datetime
import unittest2 as unittest
import ZSI
from mockito import when, any
from gites.walhebcalendar.calendar import calendar_setup
from gites.walhebcalendar.client import CalendarClient
from gites.walhebcalendar.testing import CALENDAR_ZSERVER, CALENDAR_ZCA
from gites.walhebcalendar.browser.booking import SOAPBookingManagement
from gites.walhebcalendar.browser.utils import validateARequest
from gites.walhebcalendar.zsi.booking_client import addBookingRequest
from gites.walhebcalendar.zsi.booking_server import addBookingResponse


class TestAddBooking(unittest.TestCase):
    layer = CALENDAR_ZCA

    def testValidationRequestDates(self):
        bookingRequest = addBookingRequest()
        bookingRequest._cgtId = 1
        bookingRequest._startDate = datetime(2011, 1, 2).timetuple()
        bookingRequest._endDate = datetime(2011, 1, 1).timetuple()
        msg_re = "Booking date in the past"
        with self.assertRaisesRegexp(ZSI.Fault, msg_re):
            validateARequest(bookingRequest)
        bookingRequest = addBookingRequest()
        bookingRequest._cgtId = 1
        bookingRequest._startDate = datetime(2031, 1, 2).timetuple()
        bookingRequest._endDate = datetime(2031, 1, 1).timetuple()
        msg_re = u"Start date is after end date"
        with self.assertRaisesRegexp(ZSI.Fault, msg_re):
            validateARequest(bookingRequest)

    def testWrongBookingType(self):
        bookingRequest = addBookingRequest()
        bookingRequest._cgtId = 1
        bookingRequest._startDate = datetime(2012, 1, 2).timetuple()
        bookingRequest._endDate = datetime(2012, 1, 4).timetuple()
        bookingRequest._bookingType = u'blabla'
        msg_re = u"Wrong booking type. Must be booked or ..."
        with self.assertRaisesRegexp(ZSI.Fault, msg_re):
            validateARequest(bookingRequest)


class TestFunctionalAddBooking(unittest.TestCase):
    layer = CALENDAR_ZSERVER

    def setUp(self):
        self.app = app = self.layer['app']
        calendar_setup(app)
        app['acl_users'].userFolderAddUser('user1', 'secret', ['Authenticated'], [])
        import transaction
        transaction.commit()

    def testSimpleAddBooking(self):
        calendarUrl = self.app.calendar.absolute_url()
        client = CalendarClient(calendarUrl)
        startDate = datetime(2010, 1, 1)
        endDate = datetime(2010, 1, 2)
        cgtId = 1
        response = addBookingResponse()
        response._notificationId = 1
        when(SOAPBookingManagement).addBookingRequest(any(), any()).thenReturn(response)
        response = client.addBooking(cgtId, startDate, endDate)
        self.assertEqual(response, 1)
