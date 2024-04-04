def list_of_file_names(settings_dirs, spec_option):
	global settings_paths
	
	if spec_option:
		settings_paths.append(spec_option)
		return spec_option
	else:
		for s in settings_dirs:
			settings_paths.append(os.path.join(s, 'settings.ini'))

		return settings_paths

