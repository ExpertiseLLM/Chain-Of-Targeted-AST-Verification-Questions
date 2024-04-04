def load_configurations(config_filenames, overrides=None, resolve_env=True):
    parser = ConfigurationParser(overrides)
    logging.getLogger("").handlers = []
    return _load_configurations(config_filenames, parser, resolve_env)
