def parser_flags(parser):

    """Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string."""
    return''.join('--{0}'.format(f) for f in parser._flags)
