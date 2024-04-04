def find_path_type(path):
	try:
		namaste_files = [f for f in os.listdir(path) if re.match(r'0=[^/]*$', f)]
	except OSError as e:
		return "OSError on {0}: {1}".format(path, e)
	if not len(namaste_files):
		return "no namaste files found in {0}".format(path)
	if len(namaste_files) > 1:
		return "multiple namaste files found in {0}".format(path)
	namaste_file = namaste_files[0]
	if re.match(r'0=.*/inventory\.xml$', namaste_file):
		return 'root'
	if re.match(r'0=.*/inventory\.json$', namaste_file):
		return 'object'
	if re.match(r'0=inventory\.xml$', namaste_file):
		return 'file'
	return "unknown namaste file {0}".format(nam
