# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from datetime import date
import ZSI
import grokcore.component as grok
from gites.walhebcalendar.browser.interfaces import (ISOAPRequestValidator, IAddBookingRequest,
                                                     IGetBookingRequest)


class BaseValidation(grok.Subscription):
    grok.provides(ISOAPRequestValidator)
    grok.baseclass()

    def testPastDates(self):
        if self.startDate < date.today() or self.endDate < date.today():
            raise ZSI.Fault(ZSI.Fault.Client, u"Booking date in the past")

    def testDateOrder(self):
        if self.startDate > self.endDate:
            raise ZSI.Fault(ZSI.Fault.Client, u"Start date is after end date")


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
