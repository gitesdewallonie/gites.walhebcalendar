# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from zope.component import getUtility
from zope.lifecycleevent import IObjectCreatedEvent
import grokcore.component as grok
from affinitic.zamqp.interfaces import IArrivedMessage, IPublisher
from walhebcalendar.db.interfaces import INotification
from gites.walhebcalendar.client import CalendarClient
from gites.walhebcalendar.messaging.interfaces import IGitesUpdate


class WalhebCalendarUpdater(grok.Subscription):
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


@grok.subscribe(INotification, IObjectCreatedEvent)
def publishNewNotificationToGDW(notification, event):
    if notification.notf_user_id != 'gdw':
        publisher = getUtility(IPublisher, name='booking.update')
        publisher._register()
        infos = dict(booking_type=notification.notf_booking_type,
                     cgt_id=notification.notf_cgt_id,
                     start_date=notification.notf_start_date,
                     end_date=notification.notf_end_date,
                     notf_id=notification.notf_id)
        publisher.send(infos, routing_key='gdw')
