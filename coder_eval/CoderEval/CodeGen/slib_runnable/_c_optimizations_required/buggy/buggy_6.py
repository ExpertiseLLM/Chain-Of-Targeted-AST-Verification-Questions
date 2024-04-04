def _c_optimizations_required():
	"""
	Return a true value if the C optimizations are required.

This uses the ``PURE_PYTHON`` variable as documented in `_use_c_impl`.
	"""
	return PURE_PYTHON or os.environ.get('PYTHON_PURE_PYTHON')

