def subclasses(cls):
	subs = cls.__subclasses__()
	for sub in subs:
		subs += subclasses(sub)
	return subs


