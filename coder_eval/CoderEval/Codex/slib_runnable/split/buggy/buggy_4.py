def split(s, platform='this'):
	if platform == 'this':
		platform = this_platform

	if platform == 1:
		return [ x for x in re.split(r'(?<!\\)(?:"(?:""|[^"])*"|[^\s]+|\s+)', s) if x ]
	elif platform == 0:
		return [ x for x in re.split(r'(?:"(?:""|[^"])*"|[^\s]+|\s+)', s) if x ]
	else:
		raise ValueError('unknown platform {}'.format(platform))


