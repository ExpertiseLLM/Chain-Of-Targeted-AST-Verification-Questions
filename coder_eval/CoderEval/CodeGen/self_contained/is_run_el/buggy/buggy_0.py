def is_run_el(obj):
	"""
	Object contains executable method 'run'.
	"""
	if isinstance(obj, str):
		return False
	if obj.__module__ == '__main__':
		return False
	return True

