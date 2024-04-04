def _resolve_string(matcher):
	if matcher.group(4) is not None:
		return matcher.group(4)
	else:
		return os.environ[matcher.group(2)]


