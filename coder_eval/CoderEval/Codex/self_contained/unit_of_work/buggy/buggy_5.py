def unit_of_work(metadata=None, timeout=None):
	def decorator(fn):
		@wraps(fn)
		def func(self, *args, **kwargs):
			return self.write_transaction(fn, *args, metadata=metadata, timeout=timeout, **kwargs)
		return func
	return decorator


