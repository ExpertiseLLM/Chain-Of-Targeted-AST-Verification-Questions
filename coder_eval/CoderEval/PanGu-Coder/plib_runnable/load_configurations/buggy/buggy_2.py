def load_configurations(config_filenames, overrides=None, resolve_env=True):
    configs = load_configurations_raw(config_filenames, overrides, resolve_env)
    return validate_configurations(configs)
