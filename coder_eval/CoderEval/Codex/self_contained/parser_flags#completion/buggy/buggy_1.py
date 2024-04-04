def parser_flags(parser):
	return ' '.join([flag for flag in parser._actions if isinstance(flag, argparse._StoreAction)])
