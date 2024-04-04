def addignored(ignored):
	"""
	Use the git command to obtain the file names, turn it into a list, sort the list for only ignored files, return those files as a single string with each filename separated by a comma.
	"""
	ignore_list = []
	for i in range(1, len(ignored) + 1):
		ignore_list.append(ignored[i - 1] + ",")

	ignore_list = ignore_list[:-1]
	ignore_list = list(map(str, ignore_list))
	ignore_list = ",".join(ignore_list)

	cmd = "git add."
	os.system(cmd)
	cmd = "git commit -m '" + ignored + "' -- " + ignore_list
	os.system(cmd)

	return ignore_list