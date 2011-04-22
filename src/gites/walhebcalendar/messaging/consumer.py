# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
import grokcore.component as grok
from affinitic.zamqp.consumer import Consumer
from gites.walhebcalendar.messaging.interfaces import IGitesUpdate


class WalhebCalendarUpdateConsumer(Consumer):
    grok.name('booking.update.gdw')
    queue = "booking.update.gdw"
    exchange = 'booking.update.gdw'
    exchange_type = 'direct'
    routing_key = 'import'
    connection_id = 'walhebcalendar'
    messageInterface = IGitesUpdate
