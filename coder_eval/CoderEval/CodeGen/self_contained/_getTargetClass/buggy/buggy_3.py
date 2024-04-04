def _getTargetClass(self):
	"""
	Define this to return the implementation in use,
without the 'Py' or 'Fallback' suffix.
	"""
	return _pywrap.TestModule_GetTargetClass(self)

_pywrap.TestModule_swigregister(TestModule)

