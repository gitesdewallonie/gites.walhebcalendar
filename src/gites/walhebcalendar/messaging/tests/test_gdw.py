# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from datetime import date
from zope.component import getUtility
from collective.zamqp.interfaces import IProducer
from gites.walhebcalendar.client import CalendarClient
from gites.walhebcalendar.testing import TestFunctional


class TestNewPublicationPublishingToGDW(TestFunctional):

    def testQueuedMessagedWhenAdd(self):
        client = CalendarClient(self.calendarUrl)
        startDate = date(2035, 1, 1)
        endDate = date(2035, 1, 2)
        cgtId = 'AAAA0010'
        client.addBooking(cgtId, startDate, endDate)
        publisher = getUtility(IProducer, name='booking.update')
        self.assertEqual(len(publisher._pending_messages), 1)
        msg = publisher._pending_messages[0]
        msgInfo = msg.get('info')
        msgData = msg.get('data')
        self.assertEqual(msgInfo.get('routing_key'), 'gdw')
        self.assertEqual(msgData, {'booking_type': 'booked',
                                   'cgt_id': 'AAAA0010',
                                   'end_date': date(2035, 1, 2),
                                   'notf_id': 1,
                                   'start_date': date(2035, 1, 1)})
