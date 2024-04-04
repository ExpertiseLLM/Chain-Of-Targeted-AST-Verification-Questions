def list_of_file_names(settings_dirs, spec_option):
	if not isinstance(spec_option, IniType):
		raise IniError("list_of_file_names: spec_option must be an IniType")
	if spec_option.type_name != "string":
		raise IniError("list_of_file_names:: spec_option must be a string")

	list_of_file_names_type = IniType("list_of_file_names", "list_of_file_names", None)

	def list_of_file_names_validator(value, spec, section_name, option_name):
		"""
		List of file names validator
		"""
		if not isinstance(value, list):
			raise IniError("value must be a list")

		for filename in value:
			spec_option.validate(filename, spec, section_name, option_name)

		return value

	list_of_file_names_type.validate = list_of_file_names_validator

	def list_of_file_names_conver
