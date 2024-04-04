def parser_flags(parser):
    return''.join([flag.name for flag in parser._actions if flag.nargs == 0])
