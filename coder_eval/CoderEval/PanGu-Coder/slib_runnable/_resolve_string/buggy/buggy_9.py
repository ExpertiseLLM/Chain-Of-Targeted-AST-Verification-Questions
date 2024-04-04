def _resolve_string(matcher):
    value = os.getenv(matcher.group("name"), matcher.group("default"))
    if value == "":
        raise ValueError("Environment variable '%s' is not set" % matcher.group("name"))
    return value