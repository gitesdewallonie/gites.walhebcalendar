# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
import transaction
from zope.component import getSiteManager
from zope.component import getGlobalSiteManager
from zope.container.interfaces import IObjectAddedEvent
from zope.interface import implements
from zope.processlifetime import IDatabaseOpenedWithRoot
from OFS.Folder import Folder
import grokcore.component as grok
from Products.GenericSetup.interfaces import IFilesystemImporter
from Products.GenericSetup.interfaces import IFilesystemExporter
from five.localsitemanager import make_objectmanager_site
from Products.GenericSetup.tool import SetupTool
from gites.walhebcalendar.log import logger
from gites.walhebcalendar.interfaces import ICalendarApplication
CAL_ID = 'calendar'
PAS_ID = 'acl_users'
SETUP_ID = 'app_setup'

PROFILE_ID = 'profile-gites.walhebcalendar:calendar'


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


@grok.subscribe(ICalendarApplication, IObjectAddedEvent)
def setupWiwoAfterCreation(wiwoApp, event):
    """
    make wiwo a local site
    add generic setup tool in Wiwo Application
    start task queue services
    """
    sm = getSiteManager(wiwoApp)
    if sm is getGlobalSiteManager():
        logger.info('make local site')
        make_objectmanager_site(wiwoApp)

    if hasattr(wiwoApp, SETUP_ID):
        return
    logger.info('generic setup')
    wiwoApp._setObject(SETUP_ID, SetupTool(SETUP_ID))
    setup_tool = getattr(wiwoApp, SETUP_ID)

    setup_tool.setBaselineContext(PROFILE_ID)
    setup_tool.runAllImportStepsFromProfile(PROFILE_ID)


def exportPAS(context):
    app = context.getSite()
    pas = app[PAS_ID]
    IFilesystemExporter(pas).export(context, 'PAS', True)


def importPAS(context):
    app = context.getSite()
    pas = app[PAS_ID]
    IFilesystemImporter(pas).import_(context, 'PAS', True)
    logger.info('PAS imported')
