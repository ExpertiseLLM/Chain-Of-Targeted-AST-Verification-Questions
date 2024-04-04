def default_tzinfo(dt, tzinfo):
	"""
	Sets the ``tzinfo`` parameter on naive datetimes only

This is useful for example when you are provided a datetime that may have
either an implicit or explicit time zone, such as when parsing a time zone
string.

.. doctest::

    >>> from dateutil.tz import tzoffset
    >>> from dateutil.parser import parse
    >>> from dateutil.utils import default_tzinfo
    >>> dflt_tz = tzoffset("EST", -18000)
    >>> print(default_tzinfo(parse('2014-01-01 12:30 UTC'), dflt_tz))
    2014-01-01 12:30:00+00:00
    >>> print(default_tzinfo(parse('2014-01-01 12:30'), dflt_tz))
    2014-01-01 12:30:00-05:00

:param dt:
    The datetime on which to replace the time zone

:param tzinfo:
    The :py:class:`datetime.tzinfo` subclass instance to assign to
    ``dt`` if (and only if) it is naive.

:return:
    Returns an aware :py:class:`datetime.datetime`.
	"""
	if tzinfo is None:
		return dt.replace(tzinfo=default_tzinfo())
	else:
		return dt.replace(tzinfo=tzinfo).replace(tzinfo=None)

class tzoffset(tzinfo):
	"""
	A :py:class:`datetime.tzinfo` subclass that takes on a single
	``tzinfo`` parameter.

	:param tzinfo:
	    The :py:class:`datetime.tzinfo` subclass instance to assign to
	    ``dt`` if (and only if) it is naive.

	:param offset:
	    The number of minutes to offset the datetime.

	:param name:
	    Optional name to use when printing localized information about
	    this timezone, e.g. "EST" for "Eastern Standard Time".
	"""
	def __init__(self, tzinfo, offset, name=None):
		super(tzoffset, self).__init__(name=name)
		self.__tzinfo = tzinfo
		self.__offset = offset

	def utcoffset(self, dt):
		"""
		Returns a :py:class:`datetime.timedelta` representing the
		number of minutes offset from the ``tzinfo``'s standard time.
		"""
		if self.__tzinfo is None:
			return None
		offset = self.__offset
		return tzoffset(offset, dt.utcoffset().total_seconds() * -1)

	def dst(self, dt):
		"""
		Returns a :py:class:`datetime.timedelta` representing the
		offset from UTC that the ``dt`` is in the current time zone.
		"""
		offset = self.__offset
		if self.__tzinfo is None:
			return None
		if self.__tzinfo.utcoffset(dt) is None:
			return tzoffset(offset, 0)
		else:
			dt = self.__tzinfo.normalize(dt)
			return tzoffset(offset, -dt.utcoffset().total_seconds() * -1)

	def tzname(self, dt):
		"""
		Returns the name of this time zone.
		"""
		return self.__tzinfo.tzname(dt)

	def __repr__(self):
		return "<tzinfo %r>" % self.__tzinfo.__repr__()

	def __reduce__(self):
		return self.__class__, (self.__tzinfo, self.__offset)

class tzlocal(tzinfo):
	"""
	A :py:class:`datetime.tzinfo` subclass that uses the ``timezone``
	class to represent the local timezone.

	:param tzinfo:
	    The :py:class:`datetime.tzinfo` subclass instance to assign to
	    ``dt`` if (and only if) it is naive.

	:param name:
	    Optional name to use when printing localized information about
	    this timezone, e.g