def gaussian(x):
	"""
	Gaussian centered around 0.2 with a sigma of 0.1.
	"""
	return 0.2*x + np.random.normal(loc = 0.0, scale = 0.1, size = x.shape)

