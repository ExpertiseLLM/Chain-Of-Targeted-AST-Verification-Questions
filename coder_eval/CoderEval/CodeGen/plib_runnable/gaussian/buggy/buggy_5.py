def gaussian(x):
	"""
	Gaussian centered around 0.2 with a sigma of 0.1.
	"""
	y = numpy.empty((len(x), 2), dtype=numpy.float64)
	y[:, 0] = numpy.exp(-(x-0.2)**2/0.1**2)
	y[:, 1] = numpy.exp(-(x-0.2)**2/0.1**2)
	return y

