def get(self, key, default=None):
if key in self._dict:
return self._dict[key]
else:
return default
