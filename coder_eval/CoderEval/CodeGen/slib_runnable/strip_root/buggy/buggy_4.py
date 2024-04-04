def strip_root(path, root):
	"""
	Remove root from path, throw exception on failure.
	"""
	try:
		path = os.path.join(root, path)
	except:
		raise Exception("Path '{0}' does not exist.".format(path))
	return path

from django.db import models
from django.contrib.auth.models import User