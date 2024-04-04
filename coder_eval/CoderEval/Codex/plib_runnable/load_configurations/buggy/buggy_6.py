def load_configurations(config_filenames, overrides=None, resolve_env=True):
	if overrides is None:
		overrides = {}
	config_dict = {}
	logs = []
	for cfg_filename in config_filenames:
		try:
			with open(cfg_filename, 'r') as cfg_file:
				cfg = json.load(cfg_file)
				if resolve_env:
					cfg = resolve_environment_variables(cfg)
				cfg = merge_configurations(cfg, overrides)
				validate_configuration(cfg)
				config_dict[cfg_filename] = cfg
		except Exception as e:
			logs.append(logging.LogRecord(
				name='config',
				level=logging.ERROR,
				pathname=cfg_filename,
				lineno=0,
				msg=str(e),
				args=(),
				exc_info=None
			))
	
