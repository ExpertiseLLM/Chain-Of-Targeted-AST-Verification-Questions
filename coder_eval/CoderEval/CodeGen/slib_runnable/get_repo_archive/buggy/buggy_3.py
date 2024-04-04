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
	archive = urlopen(url)
	archive_dir = Path(destination_path) / archive.read().decode('utf-8')
	archive_dir.mkdir(parents=True, exist_ok=True)
	return archive_dir

