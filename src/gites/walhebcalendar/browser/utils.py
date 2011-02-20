# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from zope.component import subscribers
from AccessControl.SecurityManagement import getSecurityManager
from gites.walhebcalendar.browser.interfaces import ISOAPRequestValidator


def validateARequest(request):
    for validator in subscribers([request], ISOAPRequestValidator):
        validator.validate()


def validate(f):

    def validateRequest(self, requestData, response):
        validateARequest(requestData)
        return f(self, requestData, response)
    validateRequest.__doc__ = f.__doc__
    return validateRequest


def getUsername():
    user = getSecurityManager().getUser()
    username = user.getUserName()
    return unicode(username)
