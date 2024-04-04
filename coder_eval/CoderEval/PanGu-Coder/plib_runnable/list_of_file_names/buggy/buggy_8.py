def list_of_file_names(settings_dirs, spec_option):
    
    
    return [IniType(file_name, spec_option) for file_name in settings_dirs]
