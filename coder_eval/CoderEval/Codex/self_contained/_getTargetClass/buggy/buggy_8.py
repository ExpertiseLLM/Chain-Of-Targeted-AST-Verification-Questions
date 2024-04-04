def _getTargetClass(self):
	impl = fallback.getImpl()
	if impl == "c":
		return PyObject
	else:
		return FallbackObject

