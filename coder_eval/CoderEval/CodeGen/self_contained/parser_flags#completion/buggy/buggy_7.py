def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	flags = ""
	for flag_group in parser._flag_groups:
		flags = flags + " ".join(flag_group.get_option_flags())
	return flags