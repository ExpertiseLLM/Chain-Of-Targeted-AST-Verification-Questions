def match(filename):
	if re.match('.*\.csv$', filename, re.IGNORECASE):
		return True
	else:
		return False


