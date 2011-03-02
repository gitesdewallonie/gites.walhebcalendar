# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
import transaction
from zope.interface import implements
from zope.processlifetime import IDatabaseOpenedWithRoot
import grokcore.component as grok
from OFS.Folder import Folder
from gites.walhebcalendar.log import logger
from gites.walhebcalendar.interfaces import ICalendarApplication
CAL_ID = 'calendar'


class Calendar(Folder):
    """
    Calendar Application
    """
    implements(ICalendarApplication)


def manage_addCalendar(container, id):
    ob = Calendar(id)
    container._setObject(id, ob)


def calendar_setup(app):
    if not hasattr(app, CAL_ID):
        logger.info('add application')
        manage_addCalendar(app, CAL_ID)
    calendar = getattr(app, CAL_ID)
    calendar.manage_permission('WalhebCalendar: Add Booking', ['Authenticated'])
    calendar.manage_permission('WalhebCalendar: View Bookings', ['Authenticated'])


@grok.subscribe(IDatabaseOpenedWithRoot)
def setupCalendar(event):
    db = event.database
    conn = db.open()
    try:
        root = conn.root()
        app = root['Application']
        try:
            calendar_setup(app)
            transaction.commit()
        except:
            transaction.abort()
            raise
    finally:
        conn.close()
