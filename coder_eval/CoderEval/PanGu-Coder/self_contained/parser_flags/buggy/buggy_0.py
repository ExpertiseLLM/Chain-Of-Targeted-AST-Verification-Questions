def parser_flags(parser):
    return''.join(flag.value for flag in parser._actions)
