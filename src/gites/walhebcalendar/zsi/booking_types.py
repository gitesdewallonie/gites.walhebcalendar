##################################################
# file: booking_types.py
#
# schema types generated by "ZSI.generate.wsdl2python.WriteServiceModule"
#    bin/wsdl2py -b src/gites/walhebcalendar/booking.wsdl -o src/gites/walhebcalendar/zsi
#
##################################################

import ZSI
import ZSI.TCcompound
from ZSI.schema import LocalElementDeclaration, ElementDeclaration, TypeDefinition, GTD, GED
from ZSI.generate.pyclass import pyclass_type

##############################
# targetNamespace
# http://affinitic.be/booking
##############################

class ns0:
    targetNamespace = "http://affinitic.be/booking"

    class addBookingRequestType_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://affinitic.be/booking"
        type = (schema, "addBookingRequestType")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = ns0.addBookingRequestType_Def.schema
            TClist = [ZSI.TC.String(pname="cgtId", aname="_cgtId", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TCtimes.gDate(pname="startDate", aname="_startDate", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TCtimes.gDate(pname="endDate", aname="_endDate", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), self.__class__.bookingType_Dec(minOccurs=0, maxOccurs=1, nillable=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                __metaclass__ = pyclass_type
                typecode = self
                def __init__(self):
                    # pyclass
                    self._cgtId = None
                    self._startDate = None
                    self._endDate = None
                    self._bookingType = None
                    return
            Holder.__name__ = "addBookingRequestType_Holder"
            self.pyclass = Holder


        class bookingType_Dec(ZSI.TC.String, LocalElementDeclaration):
            literal = "bookingType"
            schema = "http://affinitic.be/booking"
            def __init__(self, **kw):
                kw["pname"] = "bookingType"
                kw["aname"] = "_bookingType"
                ZSI.TC.String.__init__(self, **kw)
                class IHolder(str): typecode=self
                self.pyclass = IHolder
                IHolder.__name__ = "_bookingType_immutable_holder"




    class booking_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://affinitic.be/booking"
        type = (schema, "booking")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = ns0.booking_Def.schema
            TClist = [ZSI.TC.String(pname="cgtId", aname="_cgtId", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TCtimes.gDate(pname="startDate", aname="_startDate", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TCtimes.gDate(pname="endDate", aname="_endDate", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), self.__class__.bookingType_Dec(minOccurs=0, maxOccurs=1, nillable=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                __metaclass__ = pyclass_type
                typecode = self
                def __init__(self):
                    # pyclass
                    self._cgtId = None
                    self._startDate = None
                    self._endDate = None
                    self._bookingType = None
                    return
            Holder.__name__ = "booking_Holder"
            self.pyclass = Holder


        class bookingType_Dec(ZSI.TC.String, LocalElementDeclaration):
            literal = "bookingType"
            schema = "http://affinitic.be/booking"
            def __init__(self, **kw):
                kw["pname"] = "bookingType"
                kw["aname"] = "_bookingType"
                ZSI.TC.String.__init__(self, **kw)
                class IHolder(str): typecode=self
                self.pyclass = IHolder
                IHolder.__name__ = "_bookingType_immutable_holder"




    class notification_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "http://affinitic.be/booking"
        type = (schema, "notification")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = ns0.notification_Def.schema
            TClist = [ZSI.TC.String(pname="cgtId", aname="_cgtId", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TCnumbers.Iint(pname="notificationId", aname="_notificationId", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TCtimes.gDate(pname="startDate", aname="_startDate", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TCtimes.gDate(pname="endDate", aname="_endDate", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), self.__class__.bookingType_Dec(minOccurs=0, maxOccurs=1, nillable=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                __metaclass__ = pyclass_type
                typecode = self
                def __init__(self):
                    # pyclass
                    self._cgtId = None
                    self._notificationId = None
                    self._startDate = None
                    self._endDate = None
                    self._bookingType = None
                    return
            Holder.__name__ = "notification_Holder"
            self.pyclass = Holder


        class bookingType_Dec(ZSI.TC.String, LocalElementDeclaration):
            literal = "bookingType"
            schema = "http://affinitic.be/booking"
            def __init__(self, **kw):
                kw["pname"] = "bookingType"
                kw["aname"] = "_bookingType"
                ZSI.TC.String.__init__(self, **kw)
                class IHolder(str): typecode=self
                self.pyclass = IHolder
                IHolder.__name__ = "_bookingType_immutable_holder"




    class addBookingResponse_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "addBookingResponse"
        schema = "http://affinitic.be/booking"
        def __init__(self, **kw):
            ns = ns0.addBookingResponse_Dec.schema
            TClist = [ZSI.TCnumbers.Iint(pname="notificationId", aname="_notificationId", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = (u'http://affinitic.be/booking', u'addBookingResponse')
            kw["aname"] = "_addBookingResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                __metaclass__ = pyclass_type
                typecode = self
                def __init__(self):
                    # pyclass
                    self._notificationId = None
                    return
            Holder.__name__ = "addBookingResponse_Holder"
            self.pyclass = Holder

    class addBookingRequest_Dec(ElementDeclaration):
        literal = "addBookingRequest"
        schema = "http://affinitic.be/booking"
        substitutionGroup = None
        def __init__(self, **kw):
            kw["pname"] = (u'http://affinitic.be/booking', u'addBookingRequest')
            kw["aname"] = "_addBookingRequest"
            if ns0.addBookingRequestType_Def not in ns0.addBookingRequest_Dec.__bases__:
                bases = list(ns0.addBookingRequest_Dec.__bases__)
                bases.insert(0, ns0.addBookingRequestType_Def)
                ns0.addBookingRequest_Dec.__bases__ = tuple(bases)

            ns0.addBookingRequestType_Def.__init__(self, **kw)
            if self.pyclass is not None: self.pyclass.__name__ = "addBookingRequest_Dec_Holder"

    class getBookingsRequest_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "getBookingsRequest"
        schema = "http://affinitic.be/booking"
        def __init__(self, **kw):
            ns = ns0.getBookingsRequest_Dec.schema
            TClist = [ZSI.TCtimes.gDate(pname="minDate", aname="_minDate", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TCtimes.gDate(pname="maxDate", aname="_maxDate", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="cgtId", aname="_cgtId", minOccurs=0, maxOccurs="unbounded", nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = (u'http://affinitic.be/booking', u'getBookingsRequest')
            kw["aname"] = "_getBookingsRequest"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                __metaclass__ = pyclass_type
                typecode = self
                def __init__(self):
                    # pyclass
                    self._minDate = None
                    self._maxDate = None
                    self._cgtId = []
                    return
            Holder.__name__ = "getBookingsRequest_Holder"
            self.pyclass = Holder

    class getBookingsResponse_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "getBookingsResponse"
        schema = "http://affinitic.be/booking"
        def __init__(self, **kw):
            ns = ns0.getBookingsResponse_Dec.schema
            TClist = [GTD("http://affinitic.be/booking","booking",lazy=False)(pname="bookings", aname="_bookings", minOccurs=0, maxOccurs="unbounded", nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = (u'http://affinitic.be/booking', u'getBookingsResponse')
            kw["aname"] = "_getBookingsResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                __metaclass__ = pyclass_type
                typecode = self
                def __init__(self):
                    # pyclass
                    self._bookings = []
                    return
            Holder.__name__ = "getBookingsResponse_Holder"
            self.pyclass = Holder

    class getNotificationsRequest_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "getNotificationsRequest"
        schema = "http://affinitic.be/booking"
        def __init__(self, **kw):
            ns = ns0.getNotificationsRequest_Dec.schema
            TClist = [ZSI.TCnumbers.Iint(pname="minNotificationId", aname="_minNotificationId", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TCnumbers.Iint(pname="maxNotificationId", aname="_maxNotificationId", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = (u'http://affinitic.be/booking', u'getNotificationsRequest')
            kw["aname"] = "_getNotificationsRequest"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                __metaclass__ = pyclass_type
                typecode = self
                def __init__(self):
                    # pyclass
                    self._minNotificationId = None
                    self._maxNotificationId = None
                    return
            Holder.__name__ = "getNotificationsRequest_Holder"
            self.pyclass = Holder

    class getNotificationsResponse_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "getNotificationsResponse"
        schema = "http://affinitic.be/booking"
        def __init__(self, **kw):
            ns = ns0.getNotificationsResponse_Dec.schema
            TClist = [GTD("http://affinitic.be/booking","notification",lazy=False)(pname="notifications", aname="_notifications", minOccurs=0, maxOccurs="unbounded", nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = (u'http://affinitic.be/booking', u'getNotificationsResponse')
            kw["aname"] = "_getNotificationsResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                __metaclass__ = pyclass_type
                typecode = self
                def __init__(self):
                    # pyclass
                    self._notifications = []
                    return
            Holder.__name__ = "getNotificationsResponse_Holder"
            self.pyclass = Holder

    class cancelBookingRequest_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "cancelBookingRequest"
        schema = "http://affinitic.be/booking"
        def __init__(self, **kw):
            ns = ns0.cancelBookingRequest_Dec.schema
            TClist = [ZSI.TC.String(pname="cgtId", aname="_cgtId", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TCtimes.gDate(pname="startDate", aname="_startDate", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TCtimes.gDate(pname="endDate", aname="_endDate", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = (u'http://affinitic.be/booking', u'cancelBookingRequest')
            kw["aname"] = "_cancelBookingRequest"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                __metaclass__ = pyclass_type
                typecode = self
                def __init__(self):
                    # pyclass
                    self._cgtId = None
                    self._startDate = None
                    self._endDate = None
                    return
            Holder.__name__ = "cancelBookingRequest_Holder"
            self.pyclass = Holder

    class cancelBookingResponse_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "cancelBookingResponse"
        schema = "http://affinitic.be/booking"
        def __init__(self, **kw):
            ns = ns0.cancelBookingResponse_Dec.schema
            TClist = [ZSI.TCnumbers.Iint(pname="notificationId", aname="_notificationId", minOccurs=1, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = (u'http://affinitic.be/booking', u'cancelBookingResponse')
            kw["aname"] = "_cancelBookingResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                __metaclass__ = pyclass_type
                typecode = self
                def __init__(self):
                    # pyclass
                    self._notificationId = None
                    return
            Holder.__name__ = "cancelBookingResponse_Holder"
            self.pyclass = Holder

# end class ns0 (tns: http://affinitic.be/booking)
