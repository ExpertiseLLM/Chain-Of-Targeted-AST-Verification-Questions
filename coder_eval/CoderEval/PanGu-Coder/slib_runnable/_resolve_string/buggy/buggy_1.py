def _resolve_string(matcher):
    name = matcher.group(1)
    if name not in os.environ:
        raise Error("The variable %s is not defined in the environment" % name)
    return os.environ[name]
