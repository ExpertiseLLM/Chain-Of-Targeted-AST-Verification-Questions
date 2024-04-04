def make_find_paths(find_paths):
	def transform_path(path):
		if path.startswith('sh:') or path.startswith('pp:'):
			return path
		return 'sh:**/*%s*/**' % path
	return [transform_path(path) for path in find_paths]

