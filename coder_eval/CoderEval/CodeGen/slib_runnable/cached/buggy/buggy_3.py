def cached(cache, key=hashkey, lock=None):
	"""
	Decorator to wrap a function with a memoizing callable that saves
results in a cache.
	"""
	if cache is not None:
		cache = _Cache(cache)
	def wrapped(*args, **kwargs):
		try:
			return cache[key]
		except KeyError:
			result = cache.get(key, None)
			if result is None:
				result = cache.setdefault(key, wrapped(*args, **kwargs))
			cache[key] = result
			return result
	return wrapped

