def _resolve_string(matcher):
    env_name = matcher.group('name')
    env_value = os.environ.get(env_name, '')
    if env_value == '':
        raise ValueError('Missing environment variable %r' % env_name)
    return env_value
