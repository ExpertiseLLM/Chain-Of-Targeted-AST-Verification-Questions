def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
	if not overwrite and os.path.exists(config_filename):
		raise FileExistsError("File already exists: %s" % config_filename)
	directory = os.path.dirname(config_filename)
	if not os.path.exists(directory):
		os.makedirs(directory, mode=0o755)
	with open(config_filename, "w") as f:
		f.write(rendered_config)
	os.chmod(config_filename, mode)

