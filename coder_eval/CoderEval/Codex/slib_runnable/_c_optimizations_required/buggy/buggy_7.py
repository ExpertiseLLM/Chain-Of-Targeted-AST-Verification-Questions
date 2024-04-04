def _c_optimizations_required():
	global _c_optimizations_required_cache
	if _c_optimizations_required_cache is None:
		_c_optimizations_required_cache = bool(not _use_c_impl() and not PURE_PYTHON)
	return _c_optimizations_required_cache

