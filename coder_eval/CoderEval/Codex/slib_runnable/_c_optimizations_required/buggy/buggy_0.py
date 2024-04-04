def _c_optimizations_required():
	if PURE_PYTHON:
		return False
	if not _c_optimizations_available():
		return False
	return True

