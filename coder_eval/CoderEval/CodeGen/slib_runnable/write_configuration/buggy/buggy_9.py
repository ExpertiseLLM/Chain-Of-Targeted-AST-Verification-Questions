def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
	"""
	Given a target config filename and rendered config YAML, write it out to file. Create any
containing directories as needed. But if the file already exists and overwrite is False,
abort before writing anything.
	"""
	if os.path.exists(config_filename):
		if overwrite:
			os.remove(config_filename)
		else:
			raise Exception('File {} already exists!'.format(config_filename))
	
	config_dir = os.path.dirname(config_filename)
	if not os.path.exists(config_dir):
		os.makedirs(config_dir)
	
	if mode == 0o600:
		#