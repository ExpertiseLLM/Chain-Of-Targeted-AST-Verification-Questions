def is_fill_compute_el(obj):
	"""
	Object contains executable methods 'fill' and 'compute'.
	"""
	if obj.__class__.__name__ == 'Compute':
		return True
	else:
		return False

