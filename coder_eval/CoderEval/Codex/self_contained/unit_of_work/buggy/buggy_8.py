def unit_of_work(metadata=None, timeout=None):
	def decorator(f):
		@wraps(f)
		def wrapper(*args, **kwargs):
			# get the first positional argument
			# this is the transaction
			tx = args[0]
			# assign the timeout and metadata to the transaction
			tx._set_timeout(timeout)
			tx._set_metadata(metadata)
			return f(*args, **kwargs)
		return wrapper
	return decorator


