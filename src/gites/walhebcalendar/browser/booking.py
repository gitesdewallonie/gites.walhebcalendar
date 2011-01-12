# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from gites.walhebcalendar.browser.utils import validate


class SOAPBookingManagement(object):

    @validate
    def addBookingRequest(self, requestData, response):
        response._notificationId = 1
        return response
