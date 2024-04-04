def match(filename):
    return (filename in ("", "-") or
            filename.startswith("-") and
            os.path.isdir(filename[1:]))
