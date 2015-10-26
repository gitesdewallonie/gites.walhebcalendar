# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
import grokcore.component as grok
from collective.zamqp.producer import Producer


class GitesCalendarUpdatePublisher(Producer):
    grok.name('booking.update')
    connection_id = 'walhebcalendar'
    exchange = 'booking.update'
    serializer = 'pickle'
