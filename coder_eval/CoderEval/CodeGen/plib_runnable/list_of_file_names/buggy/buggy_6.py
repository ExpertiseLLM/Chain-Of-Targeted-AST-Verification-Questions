def list_of_file_names(settings_dirs, spec_option):
	"""
	Create a new IniType complex type
	"""
	file_names = []
	for d in settings_dirs:
		for root, directories, filenames in os.walk(d):
			for filename in filenames:
				if filename.endswith(spec_option):
					file_names.append(filename)
	return file_names

