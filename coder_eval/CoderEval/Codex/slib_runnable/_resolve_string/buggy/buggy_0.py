def _resolve_string(matcher):
	var_name, default = matcher.group(1), matcher.group(2)
	var_value = os.environ.get(var_name)
	if var_value is None:
		if default is None:
			raise Error("Environment variable {} is not defined".format(var_name))
		else:
			var_value = default
	return var_value

