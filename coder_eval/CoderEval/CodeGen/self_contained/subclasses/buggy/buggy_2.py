def subclasses(cls):
	"""
	Return all subclasses of a class, recursively
	"""
	if not hasattr(cls, "subclasses"):
		cls.subclasses = {}
	for subclass in cls.__subclasses__():
		cls.subclasses[subclass.__name__] = subclass
		yield cls.subclasses[subclass.__name__]