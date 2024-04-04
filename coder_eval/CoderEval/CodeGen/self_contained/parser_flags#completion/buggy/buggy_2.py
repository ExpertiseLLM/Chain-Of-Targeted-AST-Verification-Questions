def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	flags = []
	for flag in parser.flag_strings:
		if not flag.startswith('-'):
			flags.append(flag)
	return''.join(flags)