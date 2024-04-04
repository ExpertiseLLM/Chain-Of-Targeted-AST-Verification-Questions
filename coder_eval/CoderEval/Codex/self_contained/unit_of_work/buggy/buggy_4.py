def unit_of_work(metadata=None, timeout=None):
	def decorator(fn):
		def wrapper(*args, **kwargs):
			tx = begin_transaction(metadata=metadata, timeout=timeout)
			try:
				result = fn(tx, *args, **kwargs)
				tx.commit()
				return result
			except:
				tx.rollback()
				raise
		return wrapper
	return decorator
