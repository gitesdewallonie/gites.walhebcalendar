# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from zope.interface import Interface


class ISOAPRequestValidator(Interface):
    """
    Request validation
    """

    def validate():
        """
        validate a request
        """


class IBookingRequest(Interface):
    """
    Booking Request interface
    """
