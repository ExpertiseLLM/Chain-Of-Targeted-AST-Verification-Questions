def make_find_paths(find_paths):
	# pylint: disable=unused-argument
	def _make_find_paths(context):
		if context.args.find_paths:
			result = []
			for value in context.args.find_paths:
				if value.startswith('pp:'):
					result.append(value)
				else:
					result.append('sh:**/*%s*/**' % value)
			context.args.find_paths = result
	return _make_find_paths

