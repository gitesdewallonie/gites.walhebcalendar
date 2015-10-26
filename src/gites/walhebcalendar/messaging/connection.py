# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
import os
import grokcore.component as grok
from collective.zamqp.connection import BrokerConnection


def getBrokerHost():
    return os.environ.get('AMQP_BROKER_HOST', 'localhost')


class WalhebCalendarConnection(BrokerConnection):
    grok.name("walhebcalendar")
    virtual_host = "/walhebcalendar"
    hostname = getBrokerHost()
    port = 5672
    username = "admin"
    password = "walhebcalendar"
