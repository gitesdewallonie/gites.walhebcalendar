# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from datetime import datetime
import ZSI
import grokcore.component as grok
from gites.walhebcalendar.browser.interfaces import ISOAPRequestValidator, IBookingRequest


class AddBookingRequestValidation(grok.Subscription):
    grok.provides(ISOAPRequestValidator)
    grok.context(IBookingRequest)

    def __init__(self, bookingRequest):
        self.bookingRequest = bookingRequest
        self.startDate = datetime(*self.bookingRequest._startDate[:6])
        self.endDate = datetime(*self.bookingRequest._endDate[:6])

    def testPastDates(self):
        if self.startDate < datetime.now() or self.endDate < datetime.now():
            raise ZSI.Fault(ZSI.Fault.Client, u"Booking date in the past")

    def testDateOrder(self):
        if self.startDate > self.endDate:
            raise ZSI.Fault(ZSI.Fault.Client, u"Start date is after end date")

    def testBookingType(self):
        if self.bookingRequest._bookingType not in ['booked']:
            raise ZSI.Fault(ZSI.Fault.Client, u"Wrong booking type. Must be booked or ...")

    def validate(self):
        self.testPastDates()
        self.testDateOrder()
        self.testBookingType()
