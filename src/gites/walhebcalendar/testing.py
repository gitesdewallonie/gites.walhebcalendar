# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from plone.testing import z2
from walhebcalendar.db.testing import WalHebRdbWithZope, ZCMLLayer, WALHEBRDB


class Calendar(ZCMLLayer):
    import gites.walhebcalendar
    tested_package = gites.walhebcalendar

    def tearDown(self):
        raise NotImplementedError()

CALENDAR = Calendar(name="Calendar")

CALENDAR_ZSERVER = WalHebRdbWithZope(bases=(CALENDAR, WALHEBRDB, z2.ZSERVER), name='CalendarWithZServer')
