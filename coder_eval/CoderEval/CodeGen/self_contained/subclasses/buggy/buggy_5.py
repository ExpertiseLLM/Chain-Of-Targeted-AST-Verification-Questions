def subclasses(cls):
	"""
	Return all subclasses of a class, recursively
	"""
	if cls not in cls._subclasses:
		cls._subclasses.append(cls.__subclasses__()[0])
	return cls._subclasses

