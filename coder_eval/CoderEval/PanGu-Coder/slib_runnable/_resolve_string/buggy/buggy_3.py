def _resolve_string(matcher):
    env_name = matcher.group(1)
    default = matcher.group(2) if matcher.group(2) else None
    value = os.environ.get(env_name, default)
    if value is None:
        raise Error('Variable {} is not defined in environment.'.format(env_name))
    return value
