def parser_flags(parser):
	flags = []
	for action in parser._actions:
		if action.option_strings:
			flags.append(" ".join(action.option_strings))
		else:
			flags.append(action.dest)
	return " ".join(flags)

