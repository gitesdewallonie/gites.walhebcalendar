# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from zope.component import getUtility
from zope.lifecycleevent import IObjectCreatedEvent
import grokcore.component as grok
from collective.zamqp.interfaces import IMessageArrivedEvent, IProducer
from walhebcalendar.db.interfaces import INotification
from gites.walhebcalendar.client import CalendarClient
from gites.walhebcalendar.messaging.interfaces import IGitesUpdate


@grok.subscribe(IGitesUpdate, IMessageArrivedEvent)
def consumeMessage(message, event):
    updateInfos = message.body
    calendarUrl = 'http://localhost:6011/calendar'
    client = CalendarClient(calendarUrl, login='gdw', passwd='XXXXX')
    updateType = updateInfos.get('typeOfSelection')
    bookTypeTranslation = {'loue': 'booked',
                           'indisp': 'unavailable',
                           'libre': 'available'}
    client.addBooking(updateInfos.get('cgtId'),
                      updateInfos.get('start'),
                      updateInfos.get('end'),
                      bookingType=bookTypeTranslation.get(updateType))
    message.ack()


@grok.subscribe(INotification, IObjectCreatedEvent)
def publishNewNotificationToGDW(notification, event):
    if notification.notf_user_id != 'gdw':
        publisher = getUtility(IProducer, name='booking.update')
        publisher._register()
        infos = dict(booking_type=str(notification.notf_booking_type),
                     cgt_id=notification.notf_cgt_id,
                     start_date=notification.notf_start_date,
                     end_date=notification.notf_end_date,
                     notf_id=notification.notf_id)
        publisher.publish(infos, routing_key='gdw')
