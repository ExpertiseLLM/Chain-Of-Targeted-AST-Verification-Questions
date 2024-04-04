def minimalBases(classes):
	bases = list(classes)
	for i in range(len(bases)):
		for j in range(i + 1, len(bases)):
			if issubclass(bases[i], bases[j]):
				bases[j] = bases[i]
	return bases

