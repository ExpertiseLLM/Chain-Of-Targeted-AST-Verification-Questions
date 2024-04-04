def unit_of_work(metadata=None, timeout=None):
	def create_tx_function(f):
		@wraps(f)
		def tx_function(*args, **kwargs):
			tx = args[0]
			if timeout is not None:
				tx.timeout = timeout
			if metadata is not None:
				tx.metadata = metadata
			return f(*args, **kwargs)
		return tx_function
	return create_tx_function
