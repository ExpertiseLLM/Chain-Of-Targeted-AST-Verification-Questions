def _fromutc(self, dt):
	dt = self._tzinfo.fromutc(dt)
	if self._tzinfo.is_ambiguous(dt):
		dt = dt.replace(fold=1)
	return dt


