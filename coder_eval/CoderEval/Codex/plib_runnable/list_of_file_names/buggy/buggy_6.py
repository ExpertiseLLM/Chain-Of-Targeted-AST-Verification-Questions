def list_of_file_names(settings_dirs, spec_option):
	file_names = []
	for settings_dir in settings_dirs:
		if os.path.exists(settings_dir):
			for file_name in os.listdir(settings_dir):
				if file_name.endswith('.ini'):
					if spec_option:
						if spec_option in file_name:
							file_names.append(os.path.join(settings_dir, file_name))
					else:
						file_names.append(os.path.join(settings_dir, file_name))
	return file_names

