def parser_flags(parser):
    return''.join(['--%s' % a for a in parser._actions])
