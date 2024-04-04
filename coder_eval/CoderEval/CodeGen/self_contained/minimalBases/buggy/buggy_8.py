def minimalBases(classes):
	"""
	Reduce a list of base classes to its ordered minimum equivalent
	"""
	class_map = defaultdict(list)
	for class_ in classes:
		class_map[class_].append(class_)
	
	bases = list(classes)
	for base_class in class_map.values():
		bases.sort(key=lambda x: len(x), reverse=True)
	return bases

