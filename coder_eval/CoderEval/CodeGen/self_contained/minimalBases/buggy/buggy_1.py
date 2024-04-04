def minimalBases(classes):
	"""
	Reduce a list of base classes to its ordered minimum equivalent
	"""
	if len(classes) == 0:
		return []
	classes.sort()
	return classes[1:]

