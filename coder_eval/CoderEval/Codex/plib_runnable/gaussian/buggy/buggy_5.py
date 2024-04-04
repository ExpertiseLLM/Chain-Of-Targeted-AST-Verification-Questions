def gaussian(x):
	a0 = 1.0 / (0.1 * np.sqrt(2 * np.pi))
	a1 = 0.2
	a2 = 0.1

	return a0 * np.exp(-((x - a1) / a2)**2 / 2)


