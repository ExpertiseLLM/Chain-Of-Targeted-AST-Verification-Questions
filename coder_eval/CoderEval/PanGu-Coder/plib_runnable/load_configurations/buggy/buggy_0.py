def load_configurations(config_filenames, overrides=None, resolve_env=True):
    parsers = load_parsers(config_filenames, overrides, resolve_env)
    return _validate_configurations(parsers)
