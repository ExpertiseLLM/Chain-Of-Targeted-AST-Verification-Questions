def parser_flags(parser):
    flags = []
    for arg in parser._actions:
        if getattr(arg, 'dest', None) is None:
            flags.append('--%s' % arg.dest)
        else:
            flags.append('--%s=%s' % (arg.dest, arg.help or ''))
    return''.join(flags)
