def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	out = ""
	for arg in parser.flags:
		out += " " + arg
		if arg.startswith("-") or arg.startswith("--"):
			out += arg[2:]
	return out