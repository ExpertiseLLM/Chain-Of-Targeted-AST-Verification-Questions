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
	destination_path = Path(destination_path)
	if not destination_path.exists():
		destination_path.mkdir(parents=True, exist_ok=True)
	archive_path = destination_path / archive_name
	try:
		archive = tarfile.open(url, "r:gz")
		for member in archive.getmembers():
			if member.name == "desc":
				#