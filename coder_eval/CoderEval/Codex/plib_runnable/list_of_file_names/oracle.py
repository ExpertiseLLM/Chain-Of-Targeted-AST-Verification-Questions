def list_of_file_names(settings_dirs, spec_option):
    """Create a new IniType complex type
    """
    return cli.ListOfFileNames("ListOfFileNames", settings_dirs, None,
                               spec_option)
