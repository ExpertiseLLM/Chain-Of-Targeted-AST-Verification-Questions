def list_of_file_names(settings_dirs, spec_option):
	"""
	Create a new IniType complex type
	"""
	file_type = IniType()
	file_type.file_type = "ini"
	file_type.spec = spec_option
	file_type.sections = []
	file_type.file_segments = []
	for d in settings_dirs:
		file_type.sections.append(d)
		file_type.file_segments.append(d)
	return file_type

