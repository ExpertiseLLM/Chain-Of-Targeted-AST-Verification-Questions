def cached(cache, key=hashkey, lock=None):
	"""
	Decorator to wrap a function with a memoizing callable that saves
results in a cache.
	"""
	def wrapper(*args, **kwargs):
		try:
			return cache[key](*args, **kwargs)
		except KeyError:
			if lock:
				lock.acquire()
			try:
				return cache[key](*args, **kwargs)
			finally:
				if lock:
					lock.release()
	return wrapper

@cached(cache=dict(), key=hashkey)
