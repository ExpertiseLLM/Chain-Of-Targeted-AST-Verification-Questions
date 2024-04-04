def unit_of_work(metadata=None, timeout=None):
	def decorator(tx_func):
		@functools.wraps(tx_func)
		def wrapper(tx):
			if metadata is not None:
				tx.run("CALL dbms.setTXMetaData($metadata)", metadata=metadata)
			if timeout is not None:
				tx.run("CALL dbms.setTXTimeout($timeout)", timeout=timeout)
			return tx_func(tx)
		return wrapper
	return decorator



