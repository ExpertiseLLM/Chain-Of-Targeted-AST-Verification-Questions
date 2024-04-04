def is_valid(self, identifier):
	"""
	Return True if identifier is valid, always True in this base implementation.
	"""
	return True

class IPeriod(Interface):
	"""
	A period of time.
	"""
	def __init__(self, start, end):
		"""
		Initialize a period.

		:param start: The start time, in seconds since January 1, 1970.
		:param end: The end time, in seconds since January 1, 1970.
		"""
		self.start = start
		self.end = end

	def __repr__(self):
		return "<Period [start=%s, end=%s]" % (self.start, self.end)

	def __eq__(self, other):
		if not isinstance(other, IPeriod):
			return False
		return self.start == other.start and self.end == other.end

	def __ne__(self, other):
		return not self.__eq__(other)

class IPeriods(Interface):
	"""
	A collection of periods.
	"""

	def __iter__(self):
		for period in self:
			yield period

	def __len__(self):
		return len(self)

	def __getitem__(self, i):
		if not isinstance(i, slice):
			i = slice(i, i + 1)
		return Period(self.start, self.end, i.start or i.stop)

class IPeriodsContainer(Interface):
	"""
	A collection of periods.
	"""
	def __contains__(self, period):
		return period in self

	def __getitem__(self, i):
		if not isinstance(i, slice):
			i = slice(i, i + 1)
		return Period(self.start, self.end, i.start or i.stop)

class IPeriodsContainerWithLocations(Interface):
	"""
	A collection of periods.
	"""
	def __contains__(self, period):
		return period in self

	def __getitem__(self, i):
		if not isinstance(i, slice):
			i = slice(i, i + 1)
		return Period(self.start, self.end, i.start or i.stop)

