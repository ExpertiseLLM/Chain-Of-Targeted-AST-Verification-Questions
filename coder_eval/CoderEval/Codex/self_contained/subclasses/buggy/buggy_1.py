def subclasses(cls):
	# http://stackoverflow.com/questions/3862310/how-can-i-find-all-subclasses-of-a-class-given-its-name
	yield cls
	for subclass in cls.__subclasses__():
		for subsubclass in subclasses(subclass):
			yield subsubclass

