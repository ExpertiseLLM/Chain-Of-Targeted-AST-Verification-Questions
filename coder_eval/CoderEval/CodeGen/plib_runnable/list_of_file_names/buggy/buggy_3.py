def list_of_file_names(settings_dirs, spec_option):
	"""
	Create a new IniType complex type
	"""
	if spec_option == "all":
		spec_option = "all"
	else:
		spec_option = spec_option.split(',')
	#