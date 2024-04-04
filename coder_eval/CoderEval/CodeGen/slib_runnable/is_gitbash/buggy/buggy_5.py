def is_gitbash():
	"""
	returns True if you run in a Windows gitbash

:return: True if gitbash
	"""
	return "gitbash" in sys.modules or "gitbash" in sys.modules

