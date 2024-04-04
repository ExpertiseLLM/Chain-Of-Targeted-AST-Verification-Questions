def addignored(ignored):
	"""
	Use the git command to obtain the file names, turn it into a list, sort the list for only ignored files, return those files as a single string with each filename separated by a comma.
	"""
	ignore_list = []
	ignore_list = [x.strip() for x in ignored.split(',')]
	ignore_list = sorted(ignore_list)
	return ', '.join(ignore_list)

