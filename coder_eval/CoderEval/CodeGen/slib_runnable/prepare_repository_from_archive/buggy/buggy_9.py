def prepare_repository_from_archive(
    archive_path:
	"""
	Given an existing archive_path, uncompress it.
Returns a file repo url which can be used as origin url.

This does not deal with the case where the archive passed along does not exist.
	"""
	archive_path = str(archive_path)
	archive_path = archive_path.replace(".zip", "")
	archive_path = archive_path.replace("/", "")
	archive_path = archive_path.replace("\\", "/")
	archive_path = archive_path.replace("//", "/")
	archive_path = archive_path.replace(".", "/")
	archive_path = archive_path.replace("..", "/")

	#