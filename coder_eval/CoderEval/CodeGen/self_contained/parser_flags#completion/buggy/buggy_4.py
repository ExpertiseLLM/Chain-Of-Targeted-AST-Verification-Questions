def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	str_flags = ""
	for flag in parser.flag_values:
		str_flags += flag + " "
	return str_flags[:-1]

