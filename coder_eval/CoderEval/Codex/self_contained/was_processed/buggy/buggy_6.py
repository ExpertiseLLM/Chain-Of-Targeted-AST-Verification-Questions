def was_processed(processed, path_name, verbose):
	abs_path = os.path.abspath(path_name)
	if abs_path in processed:
		print("Warning: {} has already been processed".format(abs_path))
		return True
	else:
		if verbose:
			print("Processing: {}".format(abs_path))
		processed.add(abs_path)
		return False

