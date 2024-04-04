def list_of_file_names(settings_dirs, spec_option):
	"""
	Create a new IniType complex type
	"""
	file_names = []
	for settings_dir in settings_dirs:
		for root, dirs, files in os.walk(settings_dir):
			for file in files:
				if file.endswith(spec_option):
					file_names.append(os.path.join(root, file))
	return file_names

