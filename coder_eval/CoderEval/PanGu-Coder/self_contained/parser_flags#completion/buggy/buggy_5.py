def parser_flags(parser):
    flags = ''
    for arg in parser._actions:
        flags +='{}'.format(arg.dest)
    return flags
