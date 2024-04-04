def parser_flags(parser):
    flags = []
    for arg in parser._actions:
        if hasattr(arg, 'dest'):
            flags.append('--{}'.format(arg.dest))
        elif hasattr(arg, 'flags'):
            flags.extend(parser_flags(arg))
    return''.join(flags)
