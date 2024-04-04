def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
	# First, create the directory this file will live in, if needed
	config_path = os.path.dirname(config_filename)
	if not os.path.exists(config_path):
		os.makedirs(config_path)

	# Next, if the file already exists, and we're not overwriting, abort
	if os.path.exists(config_filename) and not overwrite:
		log.critical("Configuration file already exists, and overwrite not specified: " + config_filename)
		sys.exit(1)

	# Then, write the file out
	with open(config_filename, "w") as config_file:
		config_file.write(rendered_config)

	# And finally, set the permissions on the file to the requested mode
	os.chmod(config_filename, mode)


