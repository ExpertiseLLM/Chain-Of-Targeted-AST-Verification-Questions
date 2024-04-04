def _c_optimizations_ignored():
	if not _c_optimizations_required():
		return True
	return False

