def list_of_file_names(settings_dirs, spec_option):
	if isinstance(settings_dirs, str):
		settings_dirs = [settings_dirs]
	
	# Get the list of files contained in each directory
	files_list = []
	for settings_dir in settings_dirs:
		for file_name in os.listdir(settings_dir):
			full_path = os.path.join(settings_dir, file_name)
			files_list.append(full_path)
	
	# Return the list of files
	return files_list

