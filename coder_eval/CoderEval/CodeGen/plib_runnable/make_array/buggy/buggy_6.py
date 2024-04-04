def make_array(shape, dtype=np.dtype("float32")):
	"""
	Function to create an array with shape and dtype.

Parameters
----------
shape : tuple
    shape of the array to create
dtype : `numpy.dtype`
    data-type of the array to create
	"""
	try:
		array = np.empty(shape, dtype=dtype)
	except TypeError:
		array = np.array(shape, dtype=dtype)
	return array