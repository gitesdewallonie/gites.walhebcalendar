# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from time import sleep
from datetime import date, datetime
import unittest2 as unittest
import ZSI
from mockito import when, any, unstub
from zope.component import getUtility
from affinitic.db.interfaces import IDatabase
from walhebcalendar.db.booking import Booking
from walhebcalendar.db.notification import Notification
from gites.walhebcalendar.calendar import calendar_setup
from gites.walhebcalendar.client import CalendarClient
from gites.walhebcalendar.testing import CALENDAR_ZSERVER, CALENDAR
from gites.walhebcalendar.browser.booking import SOAPBookingManagement
from gites.walhebcalendar.browser.utils import validateARequest
from gites.walhebcalendar.zsi.booking_client import addBookingRequest
from gites.walhebcalendar.zsi.booking_server import addBookingResponse


class TestAddBooking(unittest.TestCase):
    layer = CALENDAR

    def testValidationRequestDates(self):
        bookingRequest = addBookingRequest()
        bookingRequest._cgtId = 1
        bookingRequest._startDate = date(2011, 1, 2)
        bookingRequest._endDate = date(2011, 1, 1)
        msg_re = "Booking date in the past"
        with self.assertRaisesRegexp(ZSI.Fault, msg_re):
            validateARequest(bookingRequest)
        bookingRequest = addBookingRequest()
        bookingRequest._cgtId = 1
        bookingRequest._startDate = date(2031, 1, 2)
        bookingRequest._endDate = date(2031, 1, 1)
        msg_re = u"Start date is after end date"
        with self.assertRaisesRegexp(ZSI.Fault, msg_re):
            validateARequest(bookingRequest)

    def testWrongBookingType(self):
        bookingRequest = addBookingRequest()
        bookingRequest._cgtId = 1
        bookingRequest._startDate = date(2012, 1, 2)
        bookingRequest._endDate = date(2012, 1, 4)
        bookingRequest._bookingType = u'blabla'
        msg_re = u"Wrong booking type. Must be booked or available or unavailable"
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

    def testWrongUser(self):
        calendarUrl = self.app.calendar.absolute_url()
        client = CalendarClient(calendarUrl, login='foobar', passwd='secret')
        startDate = date(2012, 1, 1)
        endDate = date(2012, 1, 2)
        cgtId = 10
        msg_re = 'HTTP Digest Authorization Failed'
        with self.assertRaisesRegexp(RuntimeError, msg_re):
            client.addBooking(cgtId, startDate, endDate)

    def testAnonymous(self):
        calendarUrl = self.app.calendar.absolute_url()
        client = CalendarClient(calendarUrl, login=None, passwd=None)
        startDate = date(2012, 1, 1)
        endDate = date(2012, 1, 2)
        cgtId = 10
        msg_re = 'HTTP Digest Authorization Failed'
        with self.assertRaisesRegexp(RuntimeError, msg_re):
            client.addBooking(cgtId, startDate, endDate)

    def XXtestFakeAddBooking(self):
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
        unstub()

    def testAddedBooking(self):
        calendarUrl = self.app.calendar.absolute_url()
        client = CalendarClient(calendarUrl)
        startDate = date(2012, 1, 1)
        endDate = date(2012, 1, 2)
        cgtId = 10
        notfId = client.addBooking(cgtId, startDate, endDate)
        db = getUtility(IDatabase, name='pg')
        query = db.session.query(Booking)
        self.assertEqual(query.count(), 2)
        bookings = query.order_by(Booking.book_id).all()
        self.assertEqual(bookings[0].book_cgt_id, 10)
        self.assertEqual(bookings[0].book_date, date(2012, 1, 1))
        self.assertEqual(bookings[0].book_creation_notf, notfId)
        self.failUnless(bookings[0].book_creation_date < datetime.now())
        self.assertEqual(bookings[0].book_update_date, None)
        self.assertEqual(bookings[0].book_last_update_notf, None)
        self.assertEqual(bookings[0].book_booking_type, u'booked')

    def testAddedAndUpdatedBooking(self):
        calendarUrl = self.app.calendar.absolute_url()
        client = CalendarClient(calendarUrl)
        startDate = date(2012, 1, 1)
        endDate = date(2012, 1, 2)
        cgtId = 10
        notfId = client.addBooking(cgtId, startDate, endDate)
        db = getUtility(IDatabase, name='pg')
        query = db.session.query(Booking)
        self.assertEqual(query.count(), 2)
        bookings = query.order_by(Booking.book_id).all()
        self.assertEqual(bookings[0].book_cgt_id, 10)
        self.assertEqual(bookings[0].book_date, date(2012, 1, 1))
        self.assertEqual(bookings[0].book_creation_notf, notfId)
        self.failUnless(bookings[0].book_creation_date < datetime.now())
        self.assertEqual(bookings[0].book_update_date, None)
        self.assertEqual(bookings[0].book_last_update_notf, None)
        self.assertEqual(bookings[0].book_booking_type, u'booked')
        sleep(1)
        updateNotfId = client.addBooking(cgtId, startDate, endDate, u'unavailable')
        query = db.session.query(Booking)
        self.assertEqual(query.count(), 2)
        bookings = query.order_by(Booking.book_id).all()
        self.assertEqual(bookings[0].book_cgt_id, 10)
        self.assertEqual(bookings[0].book_date, date(2012, 1, 1))
        self.assertEqual(bookings[0].book_creation_notf, notfId)
        self.failUnless(bookings[0].book_creation_date < datetime.now())
        self.failUnless(bookings[0].book_update_date < datetime.now())
        self.failUnless(bookings[0].book_creation_date < bookings[0].book_update_date)
        self.assertEqual(bookings[0].book_last_update_notf, updateNotfId)
        self.assertEqual(bookings[0].book_booking_type, u'unavailable')

    def testBookingNotificationLink(self):
        calendarUrl = self.app.calendar.absolute_url()
        client = CalendarClient(calendarUrl)
        startDate = date(2012, 1, 1)
        endDate = date(2012, 1, 2)
        cgtId = 10
        client.addBooking(cgtId, startDate, endDate)
        db = getUtility(IDatabase, name='pg')
        query = db.session.query(Notification)
        notification = query.one()
        self.assertEqual(len(notification.createdBookings), 2)
        booking = notification.createdBookings[0]
        self.assertEqual(booking.creation_notification, notification)
        self.assertEqual(booking.update_notification, None)
        client = CalendarClient(calendarUrl)
        startDate = date(2012, 1, 1)
        endDate = date(2012, 1, 1)
        cgtId = 10
        client.addBooking(cgtId, startDate, endDate, u'unavailable')
        query = db.session.query(Notification)
        notification = query.order_by(Notification.notf_id.desc()).first()
        self.assertEqual(len(notification.relatedBookings), 1)
        self.assertEqual(len(notification.createdBookings), 0)
        self.assertEqual(len(notification.updatedBookings), 1)
        booking = notification.updatedBookings[0]
        self.failUnless(booking.creation_notification.notf_id < booking.update_notification.notf_id)

    def testUpdateTwice(self):
        db = getUtility(IDatabase, name='pg')
        session = db.session
        calendarUrl = self.app.calendar.absolute_url()
        client = CalendarClient(calendarUrl)
        startDate = date(2012, 1, 1)
        endDate = date(2012, 1, 2)
        cgtId = 999
        creationNotfId = client.addBooking(cgtId, startDate, endDate)
        updateNotfId = client.addBooking(cgtId, startDate, endDate)
        sleep(2)
        query = session.query(Notification)
        self.assertEqual(query.count(), 2)
        creationNotf = query.filter(Notification.notf_id == int(creationNotfId)).one()
        updateNotf = query.filter(Notification.notf_id == int(updateNotfId)).one()
        self.assertEqual(len(creationNotf.relatedBookings), 2)
        self.assertEqual(len(updateNotf.relatedBookings), 0)

    def testAddBooking(self):
        calendarUrl = self.app.calendar.absolute_url()
        client = CalendarClient(calendarUrl)
        startDate = date(2012, 1, 1)
        endDate = date(2012, 1, 2)
        cgtId = 10
        db = getUtility(IDatabase, name='pg')
        query = db.session.query(Notification)
        self.assertEqual(query.count(), 0)
        query = db.session.query(Booking)
        self.assertEqual(query.count(), 0)
        notfId = client.addBooking(cgtId, startDate, endDate)
        self.assertEqual(notfId, 1)
        sleep(1)
        notfId = client.addBooking(cgtId, startDate, endDate)
        self.assertEqual(notfId, 2)
        query = db.session.query(Notification)
        self.assertEqual(query.count(), 2)
        notifications = query.order_by(Notification.notf_id).all()
        self.failUnless(notifications[0].notf_creation_date != notifications[1].notf_creation_date)
        self.assertEqual(notifications[0].notf_id, 1)
        self.assertEqual(notifications[1].notf_id, 2)
        self.assertEqual(notifications[0].notf_user_id, 'user1')
        self.assertEqual(notifications[0].notf_start_date, startDate)
        self.assertEqual(notifications[0].notf_end_date, endDate)
        self.assertEqual(notifications[0].notf_booking_type, 'booked')

    def testAddUnavailableBooking(self):
        calendarUrl = self.app.calendar.absolute_url()
        client = CalendarClient(calendarUrl)
        startDate = date(2012, 1, 1)
        endDate = date(2012, 1, 2)
        cgtId = 10
        notfId = client.addBooking(cgtId, startDate, endDate,
                                   bookingType='unavailable')
        self.assertEqual(notfId, 1)
        db = getUtility(IDatabase, name='pg')
        query = db.session.query(Notification)
        notification = query.one()
        self.assertEqual(notification.notf_id, 1)
        self.assertEqual(notification.notf_booking_type, 'unavailable')

    def testTestIsolation(self):
        db = getUtility(IDatabase, name='pg')
        query = db.session.query(Notification)
        self.assertEqual(query.count(), 0)
