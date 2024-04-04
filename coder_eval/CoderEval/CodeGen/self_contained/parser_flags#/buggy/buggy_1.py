def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	flags = ""
	for flag in parser.flag_values:
		flags += flag + " "
	return flags.strip()

