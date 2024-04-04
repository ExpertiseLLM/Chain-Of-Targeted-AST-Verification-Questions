def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
	"""
	Given a target config filename and rendered config YAML, write it out to file. Create any
containing directories as needed. But if the file already exists and overwrite is False,
abort before writing anything.
	"""
	if not os.path.exists(config_filename):
		raise Exception("Config file %s does not exist!" % config_filename)
	if not os.path.isfile(config_filename):
		raise Exception("Config file %s does not exist!" % config_filename)
	if os.path.exists(config_filename) and not overwrite:
		raise Exception("Config file %s already exists!" % config_filename)
	
	with open(config_filename, 'w') as f:
		f.write(rendered_config)
		
		
