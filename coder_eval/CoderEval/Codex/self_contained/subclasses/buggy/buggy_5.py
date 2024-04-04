def subclasses(cls):
	seen = set()
	queue = [cls]
	while queue:
		cls = queue.pop()
		if cls in seen:
			continue
		yield cls
		seen.add(cls)
		for c in cls.__subclasses__():
			queue.append(c)
		for s in cls.__bases__:
			queue.append(s)

