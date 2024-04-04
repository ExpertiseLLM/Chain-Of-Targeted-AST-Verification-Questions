def parser_flags(parser):
    return''.join([x.name for x in parser._actions])
