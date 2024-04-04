def load_configurations(config_filenames, overrides=None, resolve_env=True):
    validate(config_filenames, resolve_env=resolve_env)
    return _load_configurations(config_filenames, overrides)
