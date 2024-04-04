def list_of_file_names(settings_dirs, spec_option):
    
    
    return ['{}.{}'.format(x, spec_option) for x in settings_dirs]
