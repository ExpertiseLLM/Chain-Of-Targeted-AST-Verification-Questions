def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
	if os.path.exists(config_filename) and not overwrite:
		raise RuntimeError("File exists, will not overwrite: {}".format(config_filename))
	config_dir = os.path.dirname(config_filename)
	if not os.path.exists(config_dir):
		os.makedirs(config_dir, mode=0o700)
	with open(config_filename, "w") as f:
		f.write(rendered_config)
	os.chmod(config_filename, mode)

