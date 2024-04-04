def get_repo_archive(url:
	"""
	Given an url and a destination path, retrieve and extract.tar.gz archive
which contains 'desc' file for each package.
Each.tar.gz archive corresponds to an Arch Linux repo ('core', 'extra', 'community').

Args:
    url: url of the.tar.gz archive to download
    destination_path: the path on disk where to extract archive

Returns:
    a directory Path where the archive has been extracted to.
	"""
	path = Path(url)
	if not path.exists():
		return None
	if not path.is_file():
		return None
	archive_name = '{}-{}.tar.gz'.format(path.stem, path.suffix)
	archive_path = path.parent / archive_name
	if not archive_path.exists():
		return None
	if not archive_path.is_file():
		return None
	return archive_path