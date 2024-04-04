def parser_flags(parser):
	flags = set()
	for action in parser._actions:
		if action.option_strings:
			flags.update(action.option_strings)
	return " ".join(sorted(flags))


