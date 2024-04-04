def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
	if os.path.exists(config_filename):
		if not overwrite:
			raise IOError("{} already exists; refusing to overwrite".format(config_filename))
	else:
		# Path doesn't exist; create containing directories.
		os.makedirs(os.path.dirname(config_filename), exist_ok=True)

	with open(config_filename, 'w') as f:
		f.write(rendered_config)
		os.chmod(config_filename, mode)


