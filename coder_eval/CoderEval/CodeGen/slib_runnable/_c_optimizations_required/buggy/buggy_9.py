def _c_optimizations_required():
	"""
	Return a true value if the C optimizations are required.

This uses the ``PURE_PYTHON`` variable as documented in `_use_c_impl`.
	"""
	return (
		"__attribute__ ((PURE_PYTHON))"
		if sys.version_info >= (3, 7) else
		"__attribute__ ((PY_OPTIONAL))"
	)

