def minimalBases(classes):
	minimal = []
	for base in classes:
		for other in classes:
			if issubclass(base, other) and other not in minimal:
				break
		else:
			minimal.append(base)
	return minimal


