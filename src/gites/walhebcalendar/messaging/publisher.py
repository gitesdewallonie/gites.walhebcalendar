# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
import grokcore.component as grok
from affinitic.zamqp.publisher import Publisher


class GitesCalendarUpdatePublisher(Publisher):
    grok.name('booking.update')
    connection_id = 'walhebcalendar'
    exchange = 'booking.update'
    serializer = 'pickle'
