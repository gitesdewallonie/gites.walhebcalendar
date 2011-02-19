# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from plone.testing import z2
from walhebcalendar.db.testing import ZCMLLayer, WALHEBRDB


class Calendar(ZCMLLayer):
    import gites.walhebcalendar
    tested_package = gites.walhebcalendar


CALENDAR = Calendar(name="Calendar")

CALENDAR_ZSERVER = Calendar(bases=(z2.ZSERVER, WALHEBRDB, ), name='CalendarWithZServer')
