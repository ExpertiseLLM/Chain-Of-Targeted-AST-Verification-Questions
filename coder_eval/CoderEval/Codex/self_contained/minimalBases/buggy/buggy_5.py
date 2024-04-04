def minimalBases(classes):
	# Empty list has no bases
	if not classes:
		return []
	# Single element list is its own minimal base
	elif len(classes) == 1:
		return classes
	# Reduce by removing redundancies from the front
	else:
		reduced = []
		for c in classes:
			if c not in reduced:
				reduced.append(c)
		return minimalBases(reduced)



