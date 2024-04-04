def gaussian(x):
	"""
	Gaussian centered around 0.2 with a sigma of 0.1.
	"""
	x = x - x.mean()
	x = x / x.std()
	x = np.exp( -0.5 * (x**2) )
	return x