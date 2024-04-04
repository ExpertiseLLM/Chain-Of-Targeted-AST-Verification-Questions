def unit_of_work(metadata=None, timeout=None):
	def decorator(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			return _unit_of_work(func, metadata, timeout, *args, **kwargs)
		return wrapper
	return decorator


