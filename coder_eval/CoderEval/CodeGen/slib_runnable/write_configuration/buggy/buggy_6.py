def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
	"""
	Given a target config filename and rendered config YAML, write it out to file. Create any
containing directories as needed. But if the file already exists and overwrite is False,
abort before writing anything.
	"""
	config_filename = config_filename.replace("/", os.sep)
	config_filename = config_filename.replace(".yaml", ".yml")
	config_filename = config_filename.replace(".yml", ".yaml")
	if os.path.exists(config_filename):
		if overwrite:
			try:
				os.remove(config_filename)
			except Exception as e:
				logger.error(e)
				return False
		else:
			return False
	with open(config_filename, "w") as f:
		yaml.dump(rendered_config, f, default_flow_style=False)
	return True

