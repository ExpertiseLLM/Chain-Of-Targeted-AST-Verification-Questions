def _inline_r_setup(code: str):
    if code == "":
        code = "--no-r"

    sys.path.insert(0, __path__[0])
    import r

    try:
        r.__version__
    except AttributeError:
        pass
    else:
        sys.path.insert(0, __path__[0] + "/" + r.__version__)
        import r

    try:
        r.__r_version__
    except AttributeError:
        pass
    else:
        sys.path.insert(0, __path__[0] + "/" + r.__r_version__)
        import r
