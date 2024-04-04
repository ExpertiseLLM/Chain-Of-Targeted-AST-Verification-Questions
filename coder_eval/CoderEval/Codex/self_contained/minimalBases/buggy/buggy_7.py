def minimalBases(classes):
	bases = []
	for cls in classes:
		if isinstance(cls, tuple):
			cls = cls[0]
		if cls not in bases:
			bases.append(cls)
		else:
			continue
		for base in cls.__bases__:
			if base not in bases:
				bases.append(base)
	return bases

