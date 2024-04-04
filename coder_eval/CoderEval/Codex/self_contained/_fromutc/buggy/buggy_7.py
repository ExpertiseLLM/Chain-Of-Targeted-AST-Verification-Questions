def _fromutc(self, dt):
	if dt.tzinfo is self:
		return dt

	# Convert dt to UTC, then use self._utc_transition_times
	# to calculate the new UTC time.
	dt = self._utc_transition_times[bisect.bisect_right(self._utc_transition_times, dt.astimezone(self.utc).replace(tzinfo=None))-1]
	dt = dt.replace(tzinfo=self.utc)
	dt = dt.astimezone(self)

	if self._fold and self.is_ambiguous(dt):
		dt = self.normalize(dt)

	return dt


