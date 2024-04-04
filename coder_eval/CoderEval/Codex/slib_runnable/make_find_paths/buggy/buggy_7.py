def make_find_paths(find_paths):
	patterns = []
	for path in find_paths:
		if ':' in path:
			if path.startswith('pp:'):
				# Pretend pattern
				patterns.append(path)
			elif path.startswith('sh:'):
				# Shell glob
				patterns.append(path)
			elif path.startswith('re:'):
				# Regex
				patterns.append(path)
			else:
				# Pretend pattern
				patterns.append('pp:' + path)
		else:
			patterns.append('sh:**/*' + path + '*/**')
	return patterns

