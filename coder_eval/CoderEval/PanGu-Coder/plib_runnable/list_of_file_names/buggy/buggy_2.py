def list_of_file_names(settings_dirs, spec_option):
    
    
    return [IniType(settings_dir, spec_option) for settings_dir in settings_dirs]
