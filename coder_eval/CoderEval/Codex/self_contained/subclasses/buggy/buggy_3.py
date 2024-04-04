def subclasses(cls):
	for subclass in cls.__subclasses__():
		for sub in subclasses(subclass):
			yield sub
	yield cls

