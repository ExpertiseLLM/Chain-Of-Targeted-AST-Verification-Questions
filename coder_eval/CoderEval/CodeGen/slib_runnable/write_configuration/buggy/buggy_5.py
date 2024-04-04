def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
	"""
	Given a target config filename and rendered config YAML, write it out to file. Create any
containing directories as needed. But if the file already exists and overwrite is False,
abort before writing anything.
	"""
	if os.path.exists(config_filename):
		if overwrite or not os.path.isfile(config_filename):
			shutil.copyfile(config_filename, config_filename + ".copy")
		else:
			print("- Aborting - File already exists.")
			return
	
	#