def find_path_type(path):
    """Return a string indicating the type of thing at the given path.

    Return values:
        'root' - looks like an OCFL Storage Root
        'object' - looks like an OCFL Object
        'file' - a file, might be an inventory
        other string explains error description

    Looks only at "0=*" Namaste files to determine the directory type.
    """
    try:
        pyfs = open_fs(path, create=False)
    except (fs.opener.errors.OpenerError, fs.errors.CreateFailed):
        # Failed to open path as a filesystem, try enclosing directory
        # in case path is a file
        (parent, filename) = fs.path.split(path)
        try:
            pyfs = open_fs(parent, create=False)
        except (fs.opener.errors.OpenerError, fs.errors.CreateFailed) as e:
            return "path cannot be opened, and nor can parent (" + str(e) + ")"
        # Can open parent, is filename a file there?
        try:
            info = pyfs.getinfo(filename)
        except fs.errors.ResourceNotFound:
            return "path does not exist"
        if info.is_dir:
            return "directory that could not be opened as a filesystem, this should not happen"  # pragma: no cover
        return 'file'
    namastes = find_namastes(0, pyfs=pyfs)
    if len(namastes) == 0:
        return "no 0= declaration file"
    # Look at the first 0= Namaste file that is of OCFL form to determine type, if there are
    # multiple declarations this will be caught later
    for namaste in namastes:
        m = re.match(r'''ocfl(_object)?_(\d+\.\d+)$''', namaste.tvalue)
        if m:
            return 'root' if m.group(1) is None else 'object'
    return "unrecognized 0= declaration file or files (first is %s)" % (namastes[0].tvalue)
