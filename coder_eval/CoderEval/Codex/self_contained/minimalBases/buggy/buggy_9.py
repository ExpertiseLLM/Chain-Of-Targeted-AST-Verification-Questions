def minimalBases(classes):
	return [c for c in classes if not any((issubclass(c, b) for b in classes if c is not b) )]

