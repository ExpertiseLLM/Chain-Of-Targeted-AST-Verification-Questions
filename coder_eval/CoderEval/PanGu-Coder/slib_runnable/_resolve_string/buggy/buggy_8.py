def _resolve_string(matcher):
    name, default = matcher.group(1), matcher.group(2)
    try:
        return os.environ[name]
    except KeyError:
        if default:
            return default
        raise Error('Key {} not defined'.format(name))
