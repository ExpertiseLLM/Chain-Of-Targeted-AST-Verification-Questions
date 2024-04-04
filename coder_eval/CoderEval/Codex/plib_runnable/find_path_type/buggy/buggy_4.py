def find_path_type(path):
	logging.debug("find_path_type(%s)" % path)

	if not os.path.exists(path):
		return "Path %s does not exist" % path

	if os.path.isfile(path):
		return "file"

	# find all the 0=* files in the directory
	files = [f for f in os.listdir(path) if f.startswith("0=")]

	if not files:
		return "Path %s does not contain any instances of '0='" % path

	# check to see if it looks like an OCFL Object
	if len(files) > 1:
		return "Path %s contains multiple instances of '0='" % path

	if len(files) == 1:
		if files[0] != "0=ocfl_object_1.0":
			return "Path %s contains a '0=' file which is not '0=ocfl_object_1.0'" % path
		return "object"

	# check to see if it looks like a Storage Root
	for
