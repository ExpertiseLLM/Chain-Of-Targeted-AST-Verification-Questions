def parser_flags(parser):
    return''.join([
        str(arg) for arg in parser.parse_args()
    ])
