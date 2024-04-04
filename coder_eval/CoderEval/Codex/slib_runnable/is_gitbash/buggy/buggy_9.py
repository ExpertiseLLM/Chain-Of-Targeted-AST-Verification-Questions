def is_gitbash():
	if re.match(r".*MINGW.*", os.environ['TERM'], re.IGNORECASE):
		return True
	else:
		return False


