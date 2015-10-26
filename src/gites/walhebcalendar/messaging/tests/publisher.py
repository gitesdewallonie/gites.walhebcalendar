# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
import grokcore.component as grok
from gites.walhebcalendar.messaging.publisher import GitesCalendarUpdatePublisher


class TestPublisher(GitesCalendarUpdatePublisher):
    """
    We need to avoid problem with threads when accessing to _pending_messages
    property in tests
    """
    grok.name('booking.update')

    def _get_pending_messages(self):
        return self._global_pending_messages

    def _set_pending_messages(self, value):
        self._global_pending_messages = value

    _pending_messages = property(_get_pending_messages, _set_pending_messages)
