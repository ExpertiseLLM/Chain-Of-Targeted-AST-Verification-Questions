def parser_flags(parser):
	try:
		flags_str = ' '.join(parser.format_help().splitlines()[1:])
	except:
		flags_str = ''

	return flags_str


