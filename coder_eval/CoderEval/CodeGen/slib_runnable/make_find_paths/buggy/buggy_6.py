def make_find_paths(find_paths):
	"""
	Given a sequence of path fragments or patterns as passed to `--find`, transform all path
fragments into glob patterns. Pass through existing patterns untouched.

For example, given find_paths of:

  ['foo.txt', 'pp:root/somedir']

... transform that into:

  ['sh:**/*foo.txt*/**', 'pp:root/somedir']
	"""
	if isinstance(find_paths, str):
		find_paths = [find_paths]
	for path in find_paths:
		if not isinstance(path, str):
			raise TypeError("A sequence of path fragments or patterns must be passed")
		for pattern in path.split(','):
			if pattern[:4] =='sh:':
				pattern = os.path.normpath(os.path.join(os.path.dirname(__file__), pattern))
			elif pattern[:4] == 'pp:':
				pattern = os.path.normpath(os.path.join(os.path.dirname(__file__), pattern))
			yield pattern

