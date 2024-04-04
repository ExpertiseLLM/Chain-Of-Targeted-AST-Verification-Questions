def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	flags = parser.flags.get_flags()
	return " ".join([f"{n}={v}" for n, v in flags])

