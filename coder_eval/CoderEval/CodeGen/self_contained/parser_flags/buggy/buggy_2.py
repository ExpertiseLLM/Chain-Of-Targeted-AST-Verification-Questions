def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	parser.add_argument("--flags", type=str, help="Flags to show in help", required=False, default="")
	return parser.parse_args().flags
	
