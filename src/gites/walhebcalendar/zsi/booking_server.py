##################################################
# file: booking_server.py
#
# skeleton generated by "ZSI.generate.wsdl2dispatch.ServiceModuleWriter"
#      bin/wsdl2py -b src/gites/walhebcalendar/booking.wsdl -o src/gites/walhebcalendar/zsi
#
##################################################

from ZSI.schema import GED, GTD
from ZSI.TCcompound import ComplexType, Struct
from booking_types import *
from ZSI.ServiceContainer import ServiceSOAPBinding

# Messages  
addBookingRequest = GED("http://affinitic.be/booking", "addBookingRequest").pyclass

addBookingResponse = GED("http://affinitic.be/booking", "addBookingResponse").pyclass

getBookingsRequest = GED("http://affinitic.be/booking", "getBookingsRequest").pyclass

getBookingsResponse = GED("http://affinitic.be/booking", "getBookingsResponse").pyclass

getNotificationsRequest = GED("http://affinitic.be/booking", "getNotificationsRequest").pyclass

getNotificationsResponse = GED("http://affinitic.be/booking", "getNotificationsResponse").pyclass

cancelBookingRequest = GED("http://affinitic.be/booking", "cancelBookingRequest").pyclass

cancelBookingResponse = GED("http://affinitic.be/booking", "cancelBookingResponse").pyclass


# Service Skeletons
class booking(ServiceSOAPBinding):
    soapAction = {}
    root = {}

    def __init__(self, post='/bookings', **kw):
        ServiceSOAPBinding.__init__(self, post)

    def soap_addBooking(self, ps, **kw):
        request = ps.Parse(addBookingRequest.typecode)
        return request,addBookingResponse()

    soapAction['http://affinitic.be/booking/Operation'] = 'soap_addBooking'
    root[(addBookingRequest.typecode.nspname,addBookingRequest.typecode.pname)] = 'soap_addBooking'

    def soap_getBookings(self, ps, **kw):
        request = ps.Parse(getBookingsRequest.typecode)
        return request,getBookingsResponse()

    soapAction['http://affinitic.be/booking/Operation'] = 'soap_getBookings'
    root[(getBookingsRequest.typecode.nspname,getBookingsRequest.typecode.pname)] = 'soap_getBookings'

    def soap_getNotifications(self, ps, **kw):
        request = ps.Parse(getNotificationsRequest.typecode)
        return request,getNotificationsResponse()

    soapAction['http://affinitic.be/booking/Operation'] = 'soap_getNotifications'
    root[(getNotificationsRequest.typecode.nspname,getNotificationsRequest.typecode.pname)] = 'soap_getNotifications'

    def soap_cancelBooking(self, ps, **kw):
        request = ps.Parse(cancelBookingRequest.typecode)
        return request,cancelBookingResponse()

    soapAction['http://affinitic.be/booking/Operation'] = 'soap_cancelBooking'
    root[(cancelBookingRequest.typecode.nspname,cancelBookingRequest.typecode.pname)] = 'soap_cancelBooking'

