def is_fill_compute_el(obj):
	if not hasattr(obj, 'fill') or not hasattr(obj, 'compute'):
		return False
	return True

