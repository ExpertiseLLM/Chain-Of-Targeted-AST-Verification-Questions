def subclasses(cls):
	"""
	Return all subclasses of a class, recursively
	"""
	if cls.__subclasses__ is None:
		cls.__subclasses__ = {}
	return [cls.__subclasses__[cls_name] for cls_name in cls.__subclasses__]

class SubClass(object):
	"""
	A wrapper for a class that provides access to members
	"""
	def __init__(self, *args, **kwargs):
		self._args = args
		self._kwargs = kwargs
	def __getattr__(self, name):
		#