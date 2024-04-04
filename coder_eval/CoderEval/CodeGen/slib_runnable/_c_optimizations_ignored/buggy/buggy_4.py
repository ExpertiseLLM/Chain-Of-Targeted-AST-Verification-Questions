def _c_optimizations_ignored():
	"""
	The opposite of `_c_optimizations_required`.
	"""
	return [
		'__Pyx_PyObject_SetItem',
		'__Pyx_PyObject_SetAttr',
		'__Pyx_PyObject_DelAttr',
		'__Pyx_PyObject_DelAttrNS',
		'__Pyx_PyObject_DelAttrNS_old',
		'__Pyx_PyObject_SetItemNS',
		'__Pyx_PyObject_SetAttrNS',
		'__Pyx_PyObject_DelAttrNS',
		'__Pyx_PyObject_DelAttrNS_old',
		'__Pyx_PyObject_SetItemNS_old',
		'__Pyx_PyObject_SetAttrNS_old',
		'__Pyx_PyObject_DelAttrNS_old',
		'__Pyx_PyObject_DelAttrNS'
	]

_c_optimizations_required = [
	'__Pyx_PyObject_SetItem',
	'__Pyx_PyObject_SetAttr',
	'__Pyx_PyObject_DelAttr',
	'__Pyx_PyObject_DelAttrNS',
	'__Pyx_PyObject_SetItemNS',
	'__Pyx_PyObject_SetAttrNS',
	'__Pyx_PyObject_DelAttrNS',
	'__Pyx_PyObject_DelAttrNS_old',
	'__Pyx_PyObject_SetItemNS_old',
	'__Pyx_PyObject_SetAttrNS_old',
	'__Pyx_PyObject_DelAttrNS_old',
	'__Pyx_PyObject_DelAttrNS'
]

_c_optimizations_new = [
	'__Pyx_PyObject_SetItem',
	'__Pyx_PyObject_SetAttr',
	'__Pyx_PyObject_DelAttr',
	'__Pyx_PyObject_DelAttrNS',
	'__Pyx_PyObject_SetItemNS',
	'__Pyx_PyObject_SetAttrNS',
	'__Pyx_PyObject_DelAttrNS',
	'__Pyx_PyObject_DelAttrNS_old',
	'__Pyx_PyObject_SetItemNS_old',
	'__Pyx_PyObject_SetAttrNS_old',
	'__Pyx_PyObject_DelAttrNS_old',
	'__Pyx_PyObject_DelAttrNS'
]

_c_optimizations_required = [
	'__Pyx_PyObject_SetItem',
	'__Pyx_PyObject_SetAttr',
	'__Pyx_PyObject_DelAttr',
	'__Pyx_PyObject_DelAttrNS',
	'__Pyx_PyObject_SetItemNS',
	'__Pyx_PyObject_SetAttrNS',
	'__Pyx_PyObject_DelAttrNS',
	'__Pyx_PyObject_DelAttrNS_old',
	'__Pyx_PyObject_SetItemNS_old',
	'__Pyx_PyObject_SetAttrNS_old',
	'__Pyx_PyObject_DelAttrNS_old',
	'__Pyx_PyObject_DelAttrNS'
]

_c_docstrings = [
	'The object is a PyObject *',
	'The object has the following slots',
	'The object has the following slots defined via keyword',
	'The object has the following slots defined by attribute',
	'The object has the following slots defined by reference',
	'The object has the following slots defined by operator',
	'The object has the following slots defined by const',
	'The object has the following slots defined by lambda',
	'The object has the following slots defined by staticmethod',
	'The object has the following slots defined by classmethod',
	'The object has the following slots defined by __getattr__',
	'The object has the following slots defined by __getattribute__',
	'The object has the following slots defined by __getattr__',
	'The object has the following slots defined by __getattribute__',
	'