def minimalBases(classes):
	return [b for b in classes if not isSubClass(classes, b)]

