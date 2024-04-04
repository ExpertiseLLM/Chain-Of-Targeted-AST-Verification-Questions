def parser_flags(parser):
	return ' '.join(sorted([flag for flag in parser._option_string_actions.keys() if flag.startswith('-')]))

