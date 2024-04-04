def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	flags = ""
	for flag in parser._flag_string_actions:
		flags += " " + flag[0]
	return flags

