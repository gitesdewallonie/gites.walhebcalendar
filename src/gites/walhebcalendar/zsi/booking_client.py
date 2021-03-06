##################################################
# file: booking_client.py
# 
# client stubs generated by "ZSI.generate.wsdl2python.WriteServiceModule"
#     bin/wsdl2py -b src/gites/walhebcalendar/booking.wsdl -o src/gites/walhebcalendar/zsi
# 
##################################################

from booking_types import *
import urlparse, types
from ZSI.TCcompound import ComplexType, Struct
from ZSI import client
from ZSI.schema import GED, GTD
import ZSI
from ZSI.generate.pyclass import pyclass_type

# Locator
class bookingLocator:
    bookingSOAP_address = "http://dev.walhebcalendar.be"
    def getbookingSOAPAddress(self):
        return bookingLocator.bookingSOAP_address
    def getbookingSOAP(self, url=None, **kw):
        return bookingSOAPSOAP(url or bookingLocator.bookingSOAP_address, **kw)

# Methods
class bookingSOAPSOAP:
    def __init__(self, url, **kw):
        kw.setdefault("readerclass", None)
        kw.setdefault("writerclass", None)
        # no resource properties
        self.binding = client.Binding(url=url, **kw)
        # no ws-addressing

    # op: addBooking
    def addBooking(self, request, **kw):
        if isinstance(request, addBookingRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://affinitic.be/booking/Operation", **kw)
        # no output wsaction
        response = self.binding.Receive(addBookingResponse.typecode)
        return response

    # op: getBookings
    def getBookings(self, request, **kw):
        if isinstance(request, getBookingsRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://affinitic.be/booking/Operation", **kw)
        # no output wsaction
        response = self.binding.Receive(getBookingsResponse.typecode)
        return response

    # op: getNotifications
    def getNotifications(self, request, **kw):
        if isinstance(request, getNotificationsRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://affinitic.be/booking/Operation", **kw)
        # no output wsaction
        response = self.binding.Receive(getNotificationsResponse.typecode)
        return response

    # op: cancelBooking
    def cancelBooking(self, request, **kw):
        if isinstance(request, cancelBookingRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="http://affinitic.be/booking/Operation", **kw)
        # no output wsaction
        response = self.binding.Receive(cancelBookingResponse.typecode)
        return response

addBookingRequest = GED("http://affinitic.be/booking", "addBookingRequest").pyclass

addBookingResponse = GED("http://affinitic.be/booking", "addBookingResponse").pyclass

getBookingsRequest = GED("http://affinitic.be/booking", "getBookingsRequest").pyclass

getBookingsResponse = GED("http://affinitic.be/booking", "getBookingsResponse").pyclass

getNotificationsRequest = GED("http://affinitic.be/booking", "getNotificationsRequest").pyclass

getNotificationsResponse = GED("http://affinitic.be/booking", "getNotificationsResponse").pyclass

cancelBookingRequest = GED("http://affinitic.be/booking", "cancelBookingRequest").pyclass

cancelBookingResponse = GED("http://affinitic.be/booking", "cancelBookingResponse").pyclass
