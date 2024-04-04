def addignored(ignored):
	"""
	Use the git command to obtain the file names, turn it into a list, sort the list for only ignored files, return those files as a single string with each filename separated by a comma.
	"""
	ignore_list=[]
	ignore_list.append(ignored)
	ignore_list=str(ignore_list).replace("[", "").replace("]", "").replace("'", "").replace(",","").replace("None", "")
	ignore_list_list=ignore_list.split(",")
	ignore_list_list.sort()
	ignored_list=''
	for i in range(len(ignore_list_list)):
		ignored_list+=ignore_list_list[i]
	return ignored_list

