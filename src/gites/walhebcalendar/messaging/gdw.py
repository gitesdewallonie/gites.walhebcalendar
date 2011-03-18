# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
import grokcore.component as grok
from affinitic.zamqp.interfaces import IArrivedMessage
from gites.walhebcalendar.client import CalendarClient
from gites.walhebcalendar.messaging.interfaces import IGitesUpdate


class GitesCalendarUpdater(grok.Subscription):
    grok.context(IGitesUpdate)
    grok.provides(IArrivedMessage)

    def __init__(self, message):
        self.message = message
        self.updateInfos = self.message.payload
        calendarUrl = 'http://localhost:6011/calendar'
        self.client = CalendarClient(calendarUrl, login='gdw',
                                     passwd='XXXXX')
        self.update()

    def update(self):
        updateType = self.updateInfos.get('typeOfSelection')
        bookTypeTranslation = {'loue': 'booked',
                               'indisp': 'unavailable',
                               'libre': 'available'}
        self.client.addBooking(self.updateInfos.get('cgtId'),
                               self.updateInfos.get('start'),
                               self.updateInfos.get('end'),
                               bookingType=bookTypeTranslation.get(updateType))
        self.message.ack()
