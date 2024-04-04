def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	flags = ""
	for flag, value in vars(parser.flags).items():
		if value:
			flags += flag + " "
	return flags

