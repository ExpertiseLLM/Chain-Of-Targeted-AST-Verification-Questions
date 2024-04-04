def is_fill_compute_el(obj):
	"""
	Object contains executable methods 'fill' and 'compute'.
	"""
	if obj.__class__.__name__ == 'FillComputation':
		return True
	elif obj.__class__.__name__ == 'ComputeComputation':
		return True
	return False

