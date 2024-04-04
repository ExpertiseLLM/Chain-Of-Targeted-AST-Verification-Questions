def list_of_file_names(settings_dirs, spec_option):
	filenames = []
	for dirname in settings_dirs:
		for f in os.listdir(dirname):
			if f.endswith(spec_option + ".ini"):
				filenames.append(os.path.join(dirname, f))
	return filenames

