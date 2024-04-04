def gaussian(x):
	"""
	Gaussian centered around 0.2 with a sigma of 0.1.
	"""
	return 0.2*np.exp(-((x - 0.2)**2)/0.1**2)

