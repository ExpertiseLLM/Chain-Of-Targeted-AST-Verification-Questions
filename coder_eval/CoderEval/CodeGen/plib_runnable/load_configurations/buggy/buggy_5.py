def load_configurations(config_filenames, overrides=None, resolve_env=True):
	"""
	Given a sequence of configuration filenames, load and validate each configuration file. Return
the results as a tuple of: dict of configuration filename to corresponding parsed configuration,
and sequence of logging.LogRecord instances containing any parse errors.
	"""
	#