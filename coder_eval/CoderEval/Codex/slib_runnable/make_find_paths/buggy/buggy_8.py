def make_find_paths(find_paths):
	find_paths = list(find_paths)
	for i, path in enumerate(find_paths):
		if not path.startswith(('pp:', 'sh:')):
			find_paths[i] = 'sh:**/*{}*/**'.format(path)
	return find_paths

