# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from zope.configuration import xmlconfig
from plone.testing import Layer, z2, zca


class Calendar(Layer):

    def setUp(self):
        configurationContext = self['configurationContext']
        import gites.walhebcalendar
        xmlconfig.file('configure.zcml', gites.walhebcalendar, context=configurationContext)

CALENDAR_ZCA = Calendar(bases=(zca.ZCML_DIRECTIVES, ), name='CalendarWithZCMLDirective')
CALENDAR_ZSERVER = Calendar(bases=(z2.ZSERVER, ), name='CalendarWithZServer')
