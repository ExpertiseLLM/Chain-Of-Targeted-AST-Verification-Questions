def list_of_file_names(settings_dirs, spec_option):
	ini_type = new_type('file_list', 'list')
	ini_type.add_property(new_property('path', 'string'))
	ini_type.add_property(new_property('recursive', 'boolean', 'false'))
	ini_type.add_property(new_property('exclude', 'string'))
	ini_type.add_property(new_property('include', 'string'))
	ini_type.add_property(new_property('extension', 'string'))
	ini_type.add_property(new_property('ignore_hidden', 'boolean', 'true'))
	ini_type.add_property(new_property('full_path', 'boolean', 'false'))
	spec_option.type = ini_type
	return ini_type

