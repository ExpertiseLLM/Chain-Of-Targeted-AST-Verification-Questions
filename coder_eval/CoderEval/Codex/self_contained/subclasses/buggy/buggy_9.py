def subclasses(cls):
	subclasses = cls.__subclasses__()
	for subclass in subclasses:
		subclasses.extend(subclasses(subclass))
	return subclasses


