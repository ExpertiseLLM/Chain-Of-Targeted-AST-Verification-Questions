def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
	"""
	Given a target config filename and rendered config YAML, write it out to file. Create any
containing directories as needed. But if the file already exists and overwrite is False,
abort before writing anything.
	"""
	if overwrite:
		if os.path.exists(config_filename):
			os.remove(config_filename)
		if os.path.exists(config_filename+".yml"):
			os.remove(config_filename+".yml")
	else:
		if not os.path.exists(config_filename):
			os.mknod(config_filename)
		with open(config_filename+".yml", "w") as outfile:
			yaml.dump(rendered_config, outfile, default_flow_style=False)
		if not os.path.exists(config_filename+".yml"):
			print("Failed to write configuration, file not found")
			return False
	return True

