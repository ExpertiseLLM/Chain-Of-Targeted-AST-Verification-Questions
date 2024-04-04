def _resolve_string(matcher):
    name, default = matcher.groups()
    try:
        return os.environ[name]
    except KeyError:
        if default is not None:
            return default
        raise ValueError("Missing environment variable: '%s'" % name)
