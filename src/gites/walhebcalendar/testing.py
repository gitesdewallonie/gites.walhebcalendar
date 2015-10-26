# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
import unittest2 as unittest
from plone.testing import z2
from gites.walhebcalendar.calendar import calendar_setup
from walhebcalendar.db.testing import ZCMLLayer, WALHEBRDB


class Calendar(ZCMLLayer):
    import gites.walhebcalendar
    tested_package = gites.walhebcalendar

    def patchMessaging(self):
        from collective.zamqp.producer import Producer
        Producer._finish = lambda x: x

    def setUp(self):
        super(Calendar, self).setUp()
        self.patchMessaging()


CALENDAR = Calendar(name="Calendar")

CALENDAR_ZSERVER = Calendar(bases=(z2.ZSERVER, WALHEBRDB, ), name='CalendarWithZServer')


class TestFunctional(unittest.TestCase):

    layer = CALENDAR_ZSERVER

    def setUp(self):
        self.app = app = self.layer['app']
        calendar_setup(app)
        app['acl_users'].userFolderAddUser('user1', 'secret', ['Authenticated'], [])
        import transaction
        transaction.commit()
        self.calendarUrl = self.app.calendar.absolute_url()
