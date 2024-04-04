def prepare_repository_from_archive(
    archive_path:
	"""
	Given an existing archive_path, uncompress it.
Returns a file repo url which can be used as origin url.

This does not deal with the case where the archive passed along does not exist.
	"""
	
	with zipfile.ZipFile(archive_path, 'r') as archive:
		archive.extractall(os.path.dirname(archive_path))
		file_repo_url = "https://github.com/matthesmith/repository.git"
		return file_repo_url

