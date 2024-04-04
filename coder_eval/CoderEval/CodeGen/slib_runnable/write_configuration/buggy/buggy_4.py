def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
	"""
	Given a target config filename and rendered config YAML, write it out to file. Create any
containing directories as needed. But if the file already exists and overwrite is False,
abort before writing anything.
	"""
	with open(config_filename, "w") as configfile:
		configfile.write(render_config(rendered_config))
	if overwrite:
		return
	if os.path.exists(config_filename):
		if os.path.isfile(config_filename):
			os.remove(config_filename)
	os.makedirs(os.path.dirname(config_filename), exist_ok=True)
	shutil.copy2(config_filename, config_filename + ".bak")
	shutil.copy2(config_filename, config_filename)
	shutil.copy2(config_filename, config_filename + ".bak")
	shutil.copy2(config_filename, config_filename + ".bak")
	shutil.copy2(config_filename, config_filename + ".bak")