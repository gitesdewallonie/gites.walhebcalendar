# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from datetime import date
from sqlalchemy import func
import ZSI
import grokcore.component as grok
from zope.component import getUtility
from affinitic.db.interfaces import IDatabase
from walhebcalendar.db.notification import Notification
from gites.walhebcalendar.browser.interfaces import (ISOAPRequestValidator, IAddBookingRequest,
                                                     IGetBookingRequest,
                                                     IGetNotificationRequest)


class BaseValidation(grok.Subscription):
    grok.provides(ISOAPRequestValidator)
    grok.baseclass()

    def testPastDates(self):
        if self.startDate < date.today() or self.endDate < date.today():
            raise ZSI.Fault(ZSI.Fault.Client, u"Booking date in the past")

    def testDateOrder(self):
        if self.startDate > self.endDate:
            raise ZSI.Fault(ZSI.Fault.Client, u"Start date is after end date")


class GetNotificationsRequestValidation(BaseValidation):
    grok.provides(ISOAPRequestValidator)
    grok.context(IGetNotificationRequest)

    def __init__(self, notfRequest):
        self.notificationsRequest = notfRequest
        self.minNotfId = self.notificationsRequest._minNotificationId
        self.maxNotfId = self.notificationsRequest._maxNotificationId

    def validate(self):
        self.testNotfIdOrder()
        self.testSuperiorToZero()
        self.testLowerToMaxId()

    def testLowerToMaxId(self):
        db = getUtility(IDatabase, name='pg')
        query = db.session.query(func.max(Notification.notf_id).label('maxId'))
        maxNotfId = query.one().maxId
        if maxNotfId is None:
            maxNotfId = 0
        if self.minNotfId > maxNotfId or \
           (self.maxNotfId is not None and (self.maxNotfId > maxNotfId)):
            raise ZSI.Fault(ZSI.Fault.Client,
                            u"minNotificationId and maxNotificationId must be lower or equal to the current maximum notification id")

    def testSuperiorToZero(self):
        if self.minNotfId < 0 or \
           (self.maxNotfId is not None and self.maxNotfId < 0):
            raise ZSI.Fault(ZSI.Fault.Client,
                            u"minNotificationId and maxNotificationId must be higher or equal to 0")

    def testNotfIdOrder(self):
        if self.maxNotfId is not None and (self.minNotfId > self.maxNotfId):
            raise ZSI.Fault(ZSI.Fault.Client,
                            u"minNotificationId must be lower or equal to maxNotificationId")


class GetBookingRequestValidation(BaseValidation):
    grok.provides(ISOAPRequestValidator)
    grok.context(IGetBookingRequest)

    def __init__(self, bookingRequest):
        self.bookingRequest = bookingRequest
        self.startDate = self.bookingRequest._minDate
        self.endDate = self.bookingRequest._maxDate

    def validate(self):
        self.testPastDates()
        self.testDateOrder()
        self.testLargeIds()
        self.testCGTId()

    def testLargeIds(self):
        if len(self.bookingRequest._cgtId) > 1000:
            raise ZSI.Fault(ZSI.Fault.Client, u"Too many CGT ids. Maximum is 1000. If you provide no CGT id, the system will return the bookings for all CGT ids")

    def testCGTId(self):
        for cgtId in self.bookingRequest._cgtId:
            if cgtId < 0:
                raise ZSI.Fault(ZSI.Fault.Client, u"Wrong CGT Id. Must be greater than 0")


class AddBookingRequestValidation(BaseValidation):
    grok.provides(ISOAPRequestValidator)
    grok.context(IAddBookingRequest)

    def __init__(self, bookingRequest):
        self.bookingRequest = bookingRequest
        self.startDate = self.bookingRequest._startDate
        self.endDate = self.bookingRequest._endDate

    def testBookingType(self):
        if self.bookingRequest._bookingType not in ['booked', 'unavailable', 'available']:
            raise ZSI.Fault(ZSI.Fault.Client, u"Wrong booking type. Must be booked or available or unavailable")

    def testCGTId(self):
        if self.bookingRequest._cgtId < 0:
            raise ZSI.Fault(ZSI.Fault.Client, u"Wrong CGT Id. Must be greater than 0")

    def validate(self):
        self.testPastDates()
        self.testDateOrder()
        self.testBookingType()
        self.testCGTId()
