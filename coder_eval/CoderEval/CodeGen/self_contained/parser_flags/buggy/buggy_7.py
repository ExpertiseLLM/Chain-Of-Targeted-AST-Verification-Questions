def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	if hasattr(parser, 'flags'):
		return parser.flags()
	else:
		return ''

