def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	flags_str = ""
	for flag in parser.flags:
		flags_str += " " + flag
	return flags_str.strip()