def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	flags = " "
	for flag in parser._actions:
		flags += f"{flag.option_strings[0]} {flag.dest}={flag.default}"
	return flags.strip()