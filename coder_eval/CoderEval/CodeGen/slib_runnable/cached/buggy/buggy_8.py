def cached(cache, key=hashkey, lock=None):
	"""
	Decorator to wrap a function with a memoizing callable that saves
results in a cache.
	"""
	if lock is None:
		lock = Lock()

	def wrapper(fn):
		def _wrapper(*args, **kwargs):
			with lock:
				return fn(*args, **kwargs)
		return _wrapper
	return cached(cache, key=key, lock=lock)

@cached
