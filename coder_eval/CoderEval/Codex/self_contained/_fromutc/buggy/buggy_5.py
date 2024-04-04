def _fromutc(self, dt):
	if dt.tzinfo is None:
		raise ValueError("dt parameter must be timezone-aware")

	if dt.tzinfo is self:
		return dt

	if dt.tzinfo.utcoffset(dt) != self.utcoffset(dt):
		raise ValueError("Can't convert between %s and %s timezones" % (dt.tzinfo, self))

	newdt = dt.replace(tzinfo=self)

	if newdt.tzinfo is None:
		raise ValueError("%r.replace() returned an naive datetime" % dt)

	# We may have a fold here.
	if dt.fold:
		newdt = newdt.replace(fold=1)

	return newdt


