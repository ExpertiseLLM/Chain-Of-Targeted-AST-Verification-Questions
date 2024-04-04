def load_configurations(config_filenames, overrides=None, resolve_env=True):
    configs = load_configs(config_filenames, resolve_env)
    errors = validate_configs(configs, overrides=overrides)
    return configs, errors
