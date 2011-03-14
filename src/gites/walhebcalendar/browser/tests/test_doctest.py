# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
import unittest2 as unittest
import doctest
from gites.walhebcalendar.testing import CALENDAR_ZSERVER


def setUp(test):
    from gites.walhebcalendar.calendar import calendar_setup
    app = CALENDAR_ZSERVER['app']
    calendar_setup(app)
    calendarUrl = app.calendar.absolute_url()
    app['acl_users'].userFolderAddUser('user1', 'secret', ['Authenticated'], [])
    test.globs['calendarUrl'] = calendarUrl
    print app


def test_suite():
    suite = unittest.TestSuite()
    doctestSuite = doctest.DocFileSuite(
            'addbooking.txt',
            'getbookings.txt',
            setUp=setUp,
            optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE,
        )
    suite.addTests(doctestSuite)
    suite.layer = CALENDAR_ZSERVER
    return suite
