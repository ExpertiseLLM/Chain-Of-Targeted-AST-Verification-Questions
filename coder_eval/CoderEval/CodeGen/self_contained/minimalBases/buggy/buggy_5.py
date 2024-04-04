def minimalBases(classes):
	"""
	Reduce a list of base classes to its ordered minimum equivalent
	"""
	if not classes:
		return []
	classes = list(classes)
	classes.sort()
	for base in classes:
		if base == '__new__':
			continue
		for base2 in classes:
			if base2 == '__new__':
				continue
			if base == base2:
				continue
			if base!= base2 and all(base == b for b in classes):
				classes.remove(base)
				classes.remove(base2)
	return classes

