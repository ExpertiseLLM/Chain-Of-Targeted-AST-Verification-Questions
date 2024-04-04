def minimalBases(classes):
	if not classes:
		return []

	# Sort the classes
	orderedClasses = sorted(classes, key=lambda cls: cls.__name__)

	# Remove any class that is a subclass of another
	filteredClasses = []
	for cls in orderedClasses:
		for other in filteredClasses:
			if issubclass(cls, other):
				break
		else:
			filteredClasses.append(cls)

	return filteredClasses

