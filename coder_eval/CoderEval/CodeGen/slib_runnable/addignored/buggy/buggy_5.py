def addignored(ignored):
	"""
	Use the git command to obtain the file names, turn it into a list, sort the list for only ignored files, return those files as a single string with each filename separated by a comma.
	"""
	list = []
	for root, dirs, files in os.walk('./'):
		for file in files:
			if file.endswith(".git"):
				list.append(os.path.join(root, file))
	list.sort()
	return list