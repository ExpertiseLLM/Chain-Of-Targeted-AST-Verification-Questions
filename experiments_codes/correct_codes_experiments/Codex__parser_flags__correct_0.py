def parser_flags(parser):
	flags = []
	for action in parser._actions:
		if not action.option_strings:
			continue
		flags.extend(action.option_strings)
	return ' '.join(flags)

