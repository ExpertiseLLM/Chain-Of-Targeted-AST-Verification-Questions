def parser_flags(parser):
	return " ".join(sorted(
		# parser.format_argument_defaults is only available in Python 3.3+
		"{} {}".format(
			action.option_strings[0],
			parser.format_argument_defaults(action) if hasattr(parser, "format_argument_defaults") else action.default
		)
		for action in parser._actions if action.option_strings
	))

