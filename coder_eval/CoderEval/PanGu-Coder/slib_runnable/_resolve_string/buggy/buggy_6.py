def _resolve_string(matcher):
    name, default = matcher.group(1, 2)
    if default is None:
        raise EnvironmentError("Could not resolve '%s'" % name)
    return os.environ.get(name, default)
