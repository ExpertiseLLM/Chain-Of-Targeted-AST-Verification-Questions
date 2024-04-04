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
	if type(shape) == tuple:
		if len(shape)!= 2:
			raise TypeError("Only 2 dimensions are supported")
	else:
		raise TypeError("Shape must be a tuple")
	if type(dtype) == type(np.float32):
		if dtype == np.float32:
			return np.zeros(shape, dtype=np.float32)
		else:
			raise TypeError("Convert dtype to float32 is not supported")
	else:
		raise TypeError("dtype must be a numpy.dtype")

