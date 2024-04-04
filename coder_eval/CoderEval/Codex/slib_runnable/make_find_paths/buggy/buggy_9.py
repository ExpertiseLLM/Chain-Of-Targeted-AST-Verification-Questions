def make_find_paths(find_paths):
	transformed_find_paths = []
	for path in find_paths:
		if path.startswith("pp:") or path.startswith("sh:"):
			# Pass through any patterns untouched.
			transformed_find_paths.append(path)
		else:
			# Transform any path fragments into glob patterns.
			transformed_find_paths.append("sh:**/*{}*/**".format(path))
	return transformed_find_paths


