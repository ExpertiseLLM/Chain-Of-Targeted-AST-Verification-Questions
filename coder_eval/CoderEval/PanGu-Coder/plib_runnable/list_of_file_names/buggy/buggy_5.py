def list_of_file_names(settings_dirs, spec_option):
    return [
        settings_dir + spec_option + "." + ext
        for settings_dir in settings_dirs
        for ext in ["", ".py"]
    ]
