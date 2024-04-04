def list_of_file_names(settings_dirs, spec_option):
	if not isinstance(settings_dirs, list):
		raise Exception("settings_dirs must be a list")

	if not isinstance(spec_option, str):
		raise Exception("spec_option must be a string")

	options_list = []
	for settings_dir in settings_dirs:
		options_list.append(os.path.join(settings_dir, spec_option))

	return options_list


