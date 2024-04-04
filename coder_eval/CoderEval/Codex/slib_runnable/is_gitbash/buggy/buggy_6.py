def is_gitbash():
	# get current platform
	platform = sys.platform
	if platform in ["win32", "cygwin"]:
		# if platform is windows, check if gitbash is used or not
		if os.getenv("MSYSTEM") is not None:
			return True
		else:
			return False
	else:
		return False


