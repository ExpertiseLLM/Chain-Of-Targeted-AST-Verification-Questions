def load_configurations(config_filenames, overrides=None, resolve_env=True):
    cfg = load_config_files(config_filenames, resolve_env=resolve_env)
    return _validate_config_files(cfg, overrides)
