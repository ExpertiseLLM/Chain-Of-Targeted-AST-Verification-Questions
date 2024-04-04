def was_processed(processed, path_name, verbose):
	"""
	Check if a file or directory has already been processed.

To prevent recursion, expand the path name to an absolution path
call this function with a set that will store all the entries and
the entry to test. If the entry is already in the set, report the issue
and return ``True``. Otherwise, add the entry to the set and return
``False`` to allow the path to be processed.

Args:
    processed: Set to store processed pathnames
    path_name: Path to a directory or file
    verbose: True if verbose output is requested

Returns:
    True if it's already in the set. False if not.
	"""
	if isinstance(path_name, str):
		path_name = absolutepath(path_name)

	if verbose:
		print(f'[{datetime.now()}] {path_name}')

	if path_name in processed:
		return True
	elif isdir(path_name):
		if verbose:
			print(f'[{datetime.now()}] {path_name} is a directory')
		return True
	else:
		processed.add(path_name)
		return False

