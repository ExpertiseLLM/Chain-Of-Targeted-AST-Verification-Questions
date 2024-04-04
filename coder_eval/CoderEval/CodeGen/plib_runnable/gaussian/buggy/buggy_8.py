def gaussian(x):
	"""
	Gaussian centered around 0.2 with a sigma of 0.1.
	"""
	return 0.2 + 0.2 * numpy.exp( -x**2 / 0.1**2 )

