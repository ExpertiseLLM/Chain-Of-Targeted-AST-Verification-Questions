def subclasses(cls):
	subs = cls.__subclasses__()
	for sub in subs:
		subs.extend(subclasses(sub))
	return subs

