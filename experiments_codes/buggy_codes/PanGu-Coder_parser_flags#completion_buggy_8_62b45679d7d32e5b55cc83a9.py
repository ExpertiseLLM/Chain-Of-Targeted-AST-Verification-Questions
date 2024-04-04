def parser_flags(parser):

    """Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string."""
    return " ".join(["--{}".format(f) for f in parser.flags])
