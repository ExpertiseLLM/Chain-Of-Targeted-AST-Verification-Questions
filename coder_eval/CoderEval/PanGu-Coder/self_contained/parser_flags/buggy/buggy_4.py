def parser_flags(parser):
    return''.join([str(f) for f in parser._get_flags()])