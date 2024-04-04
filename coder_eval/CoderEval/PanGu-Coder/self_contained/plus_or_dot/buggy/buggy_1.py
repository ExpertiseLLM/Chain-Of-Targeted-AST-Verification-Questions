def plus_or_dot(pieces):
    if not pieces:
        return ". "
    return "+ {}".format(pieces[0])
