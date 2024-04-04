def get(self, key, default=None):
	if key in self:
		return self[key]
	return default

