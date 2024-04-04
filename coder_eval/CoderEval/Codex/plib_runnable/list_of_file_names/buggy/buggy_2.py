def list_of_file_names(settings_dirs, spec_option):
	if not spec_option:
		return []

	files_to_read = []
	for dir_path in settings_dirs:
		for file_name in os.listdir(dir_path):
			if file_name.endswith(spec_option):
				files_to_read.append(os.path.join(dir_path, file_name))
	return files_to_read


