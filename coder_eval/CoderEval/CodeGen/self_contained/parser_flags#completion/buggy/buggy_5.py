def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	flags = ""
	for flag in parser._flag_values:
		if not flag.startswith("-"):
			flags += flag + " "
	return flags[:-1]