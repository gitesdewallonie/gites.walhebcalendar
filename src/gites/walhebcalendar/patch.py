# -*- coding: utf-8 -*-
"""
gites.walhebcalendar

Licensed under the GPL license, see LICENCE.txt for more details.
Copyright by Affinitic sprl
"""
from ZSI.TCtimes import Gregorian, _fix_timezone
from datetime import date, datetime
from ZSI import _floattypes, _inttypes
from time import gmtime as _gmtime


def get_formatted_content_with_date(self, pyobj):
    if type(pyobj) in _floattypes or type(pyobj) in _inttypes:
        pyobj = _gmtime(pyobj)

    if self.fix_timezone:
        pyobj = _fix_timezone(pyobj, tz_from=None, tz_to="Z")

    d = {}
    if isinstance(pyobj, (datetime, date)):
        pyobj = pyobj.timetuple()
    else:
        pyobj = tuple(pyobj)
    if 1 in map(lambda x: x < 0, pyobj[0:6]):
        pyobj = map(abs, pyobj)
        d['neg'] = '-'
    else:
        d['neg'] = ''

    d = {}
    for k, i in [('Y', 0), ('M', 1), ('D', 2), ('h', 3), ('m', 4), ('s', 5)]:
        d[k] = pyobj[i]

    ms = pyobj[6]
    if not ms or not hasattr(self, 'format_ms'):
        return self.format % d

    if  ms > 999:
        raise ValueError('milliseconds must be a integer between 0 and 999')

    d['ms'] = ms
    return self.format_ms % d

Gregorian.get_formatted_content = get_formatted_content_with_date

from ZSI import EvaluateException
from ZSI.TCtimes import _dict_to_tuple, _fix_none_fields


def text_to_data(self, text, elt, ps):
    '''convert text into typecode specific data.
    '''
    if text is None:
        return None
    m = self.lex_pattern.match(text)
    if not m:
        raise EvaluateException('Bad Gregorian: %s' %text, ps.Backtrace(elt))
    try:
        retval = _dict_to_tuple(m.groupdict())
    except ValueError:
        raise

    if self.fix_timezone:
        retval = _fix_timezone(retval, tz_from = m.groupdict().get('tz'), tz_to = None)

    retval = _fix_none_fields(retval)

    if self.pyclass is not None:
        return self.pyclass(retval)
    if isinstance(self, gDate):
        from datetime import date
        return date(*retval[:3])
    return retval

from ZSI.TCtimes import gDate
gDate.text_to_data = text_to_data
