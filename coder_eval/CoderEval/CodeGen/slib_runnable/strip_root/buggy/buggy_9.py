def strip_root(path, root):
	"""
	Remove root from path, throw exception on failure.
	"""
	try:
		path = os.path.abspath(path)
		return os.path.join(path, os.path.splitdrive(path)[1])
	except:
		raise Exception("Error removing root from path")
	
