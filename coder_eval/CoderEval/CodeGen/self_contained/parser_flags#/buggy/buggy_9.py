def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	flags = ""
	for _, _, v in parser._actions:
		flags += v.get("help") + " "
	return flags.strip()

