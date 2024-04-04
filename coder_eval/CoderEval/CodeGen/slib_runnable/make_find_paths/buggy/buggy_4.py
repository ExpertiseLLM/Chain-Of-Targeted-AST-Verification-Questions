def make_find_paths(find_paths):
	"""
	Given a sequence of path fragments or patterns as passed to `--find`, transform all path
fragments into glob patterns. Pass through existing patterns untouched.

For example, given find_paths of:

  ['foo.txt', 'pp:root/somedir']

... transform that into:

  ['sh:**/*foo.txt*/**', 'pp:root/somedir']
	"""
	def make_path(path):
		if path.startswith('/'):
			return '*' + path[1:]
		else:
			return path
	def make_pattern(pattern):
		if pattern.startswith('/'):
			return '*' + pattern[1:]
		else:
			return pattern
	def make_paths(paths):
		ret = []
		for path in paths:
			if isinstance(path, list):
				for p in path:
					ret.append(make_path(p))
			else:
				ret.append(make_path(path))
		return ret
	return make_paths(find_paths)

