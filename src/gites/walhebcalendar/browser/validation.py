# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from datetime import date
import ZSI
import grokcore.component as grok
from gites.walhebcalendar.browser.interfaces import ISOAPRequestValidator, IBookingRequest


class AddBookingRequestValidation(grok.Subscription):
    grok.provides(ISOAPRequestValidator)
    grok.context(IBookingRequest)

    def __init__(self, bookingRequest):
        self.bookingRequest = bookingRequest
        self.startDate = self.bookingRequest._startDate
        self.endDate = self.bookingRequest._endDate

    def testPastDates(self):
        if self.startDate < date.today() or self.endDate < date.today():
            raise ZSI.Fault(ZSI.Fault.Client, u"Booking date in the past")

    def testDateOrder(self):
        if self.startDate > self.endDate:
            raise ZSI.Fault(ZSI.Fault.Client, u"Start date is after end date")

    def testBookingType(self):
        if self.bookingRequest._bookingType not in ['booked', 'unavailable', 'available']:
            raise ZSI.Fault(ZSI.Fault.Client, u"Wrong booking type. Must be booked or available or unavailable")

    def testCGTId(self):
        if self.bookingRequest < 0:
            raise ZSI.Fault(ZSI.Fault.Client, u"Wrong CGT Id. Must be greater than 0")

    def validate(self):
        self.testPastDates()
        self.testDateOrder()
        self.testBookingType()
        self.testCGTId()
