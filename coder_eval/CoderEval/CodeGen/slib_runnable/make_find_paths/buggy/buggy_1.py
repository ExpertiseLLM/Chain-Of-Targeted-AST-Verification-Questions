def make_find_paths(find_paths):
	"""
	Given a sequence of path fragments or patterns as passed to `--find`, transform all path
fragments into glob patterns. Pass through existing patterns untouched.

For example, given find_paths of:

  ['foo.txt', 'pp:root/somedir']

... transform that into:

  ['sh:**/*foo.txt*/**', 'pp:root/somedir']
	"""
	def transform(p):
		if isinstance(p, list):
			return [transform(p_) for p_ in p]
		return p
	return map(transform, find_paths)

