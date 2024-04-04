def parser_flags(parser):
	return ' '.join(map(lambda x: x.lstrip('-').upper(), parser.get_default_values().__dict__.values()))

