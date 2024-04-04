def minimalBases(classes):
	"""
	Reduce a list of base classes to its ordered minimum equivalent
	"""
	minBases = []
	for c in classes:
		if c not in minBases:
			minBases.append(c)

	return minBases

