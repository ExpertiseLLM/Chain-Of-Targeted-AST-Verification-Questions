def list_of_file_names(settings_dirs, spec_option):
    
    
    return [IniType(settings_dirs, spec_option, f)
            for f in list_of_files(settings_dirs, spec_option)]
