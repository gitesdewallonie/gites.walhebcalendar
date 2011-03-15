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


class IAddBookingRequest(Interface):
    """
    Add booking Request marker interface
    """


class IGetBookingRequest(Interface):
    """
    Get booking Request marker interface
    """


class IGetNotificationRequest(Interface):
    """
    Get notifications Request marker interface
    """


class ICancelBookingRequest(Interface):
    """
    Cancel booking Request marker interface
    """
