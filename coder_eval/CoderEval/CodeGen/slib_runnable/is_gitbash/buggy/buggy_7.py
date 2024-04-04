def is_gitbash():
	"""
	returns True if you run in a Windows gitbash

:return: True if gitbash
	"""
	return os.getenv("GITBASH_EXE", False)!= ""