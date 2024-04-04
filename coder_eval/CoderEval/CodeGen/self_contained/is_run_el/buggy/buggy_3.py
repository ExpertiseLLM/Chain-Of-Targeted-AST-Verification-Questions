def is_run_el(obj):
	"""
	Object contains executable method 'run'.
	"""
	if not isinstance(obj, BaseProcess):
		raise TypeError('{!r} is not a BaseProcess'.format(obj))

	if not hasattr(obj, 'run'):
		raise AttributeError('{!r} does not have an attribute \'run\''.format(obj))

	if not hasattr(obj, '__call__'):
		raise AttributeError('{!r} does not have a method \'__call__\''.format(obj))

	return True

