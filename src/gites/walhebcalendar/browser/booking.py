# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from zope.component import getUtility
from affinitic.db.interfaces import IDatabase
from gites.walhebcalendar.browser.utils import validate


class SOAPBookingManagement(object):

    @validate
    def addBookingRequest(self, requestData, response):
        response._notificationId = 1
        db = getUtility(IDatabase, 'pg')
        session = db.session
        import pdb;pdb.set_trace()
        return response
