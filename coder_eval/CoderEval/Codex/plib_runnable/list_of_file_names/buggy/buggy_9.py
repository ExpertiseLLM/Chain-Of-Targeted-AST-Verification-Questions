def list_of_file_names(settings_dirs, spec_option):
	
	file_names = []
	for settings_dir in settings_dirs:
		for file_name in os.listdir(settings_dir):
			if file_name.endswith('.ini'):
				file_names.append(file_name)
				
	return file_names


