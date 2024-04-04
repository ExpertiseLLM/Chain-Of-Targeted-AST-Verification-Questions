def _resolve_string(matcher):
    try:
        return os.environ[matcher.name]
    except KeyError:
        if matcher.default is not None:
            return matcher.default
        raise ValueError("Variable not defined: {}".format(matcher.name))
