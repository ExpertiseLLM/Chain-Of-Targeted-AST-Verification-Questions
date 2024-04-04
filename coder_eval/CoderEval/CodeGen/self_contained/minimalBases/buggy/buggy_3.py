def minimalBases(classes):
	"""
	Reduce a list of base classes to its ordered minimum equivalent
	"""
	def get_min_base(base):
		if base == '__main__':
			return '__main__'
		if base == 'builtins':
			return '__builtin__'
		if base == 'exceptions':
			return 'builtins'
		return base
	return sorted(classes, key=get_min_base)

