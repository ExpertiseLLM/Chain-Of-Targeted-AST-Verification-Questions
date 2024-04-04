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
	archive_name = os.path.join(destination_path, 'archive.tar.gz')
	
	#