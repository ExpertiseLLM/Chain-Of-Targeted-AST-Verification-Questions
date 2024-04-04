def subclasses(cls):
	subs = cls.__subclasses__()
	return subs + [g for s in subs for g in subclasses(s)]


