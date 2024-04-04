def make_find_paths(find_paths):
	import re
	def is_glob(p):
		return re.match(r'[*?\[\]{}]', p)
	def is_pp(p):
		return p.startswith('pp:')
	def is_sh(p):
		return p.startswith('sh:')
	def is_path_fragment(p):
		return not is_glob(p) and not is_pp(p) and not is_sh(p)
	def path_fragment_to_glob_pattern(p):
		return 'sh:**/*{}*/**'.format(p)
	return [
		path_fragment_to_glob_pattern(p)
		if is_path_fragment(p)
		else p
		for p in find_paths
	]

