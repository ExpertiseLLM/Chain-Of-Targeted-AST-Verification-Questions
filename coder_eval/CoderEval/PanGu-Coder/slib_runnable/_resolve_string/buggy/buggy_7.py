def _resolve_string(matcher):
    if matcher.name in os.environ:
        return os.environ[matcher.name]
    if matcher.default is not None:
        return matcher.default
    raise errors.Error('No default for {}'.format(matcher.name))
