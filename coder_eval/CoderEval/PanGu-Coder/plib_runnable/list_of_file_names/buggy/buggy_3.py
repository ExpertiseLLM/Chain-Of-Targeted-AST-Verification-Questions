def list_of_file_names(settings_dirs, spec_option):
    
    
    if spec_option == 'local':
        return list_of_file_names_local(settings_dirs)
    if spec_option =='remote':
        return list_of_file_names_remote(settings_dirs)
    raise ValueError('Unknown ini file type specified: {}'.format(spec_option))
