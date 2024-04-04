def prepare_repository_from_archive(
    archive_path:
	"""
	Given an existing archive_path, uncompress it.
Returns a file repo url which can be used as origin url.

This does not deal with the case where the archive passed along does not exist.
	"""
	from zipfile import ZipFile
	from pathlib import Path
	from urllib.parse import urlparse
	from datetime import datetime
	from pathlib import Path
	from os import remove
	from os.path import dirname, basename, normpath, join, isdir, isfile, exists

	def is_archive_archive(archive_path: str):
		return archive_path.endswith("/")

	def is_archive(archive_path: str):
		return is_archive_archive(archive_path)

	def get_archive_path(archive_url: str):
		"""
		Given an archive url, returns the path to the archive.
		"""
		url = urlparse(archive_url)
		if url.path.startswith("/"):
			archive_path = url.path
		else:
			archive_path = join(dirname(archive_url), url.path)
		return archive_path

	def create_dir(archive_path: str):
		"""
		Given an archive path, creates the directory in the given path.
		"""
		archive_path = get_archive_path(archive_path)
		Path(dirname(archive_path)).mkdir(parents=True, exist_ok=True)

	def create_archive(archive_path: str):
		"""
		Given an archive path, creates an archive.
		"""
		archive_path = get_archive_path(archive_path)
		with ZipFile(archive_path, "w") as archive:
			archive.write(archive_path)

	def archive_archive(archive_path: str):
		"""
		Given an archive path, uncompresses the archive.
		"""
		archive_path = get_archive_path(archive_path)
		with ZipFile(archive_path, "r") as archive:
			archive.extractall()

	def get_or_create_dir(archive_path: str):
		"""
		Given an archive path, returns the directory that was passed in.
		"""
		archive_path = get_archive_path(archive_path)
		if isdir(archive_path):
			return archive_path
		else:
			create_dir(archive_path)
			return archive_path

	def get_archive_url(archive_path: str):
		"""
		Given an archive path, returns the url for the archive.
		"""
		archive_path = get_archive_path(archive_path)
		return urlparse(archive_path).scheme + "://" + urlparse(archive_path).netloc + archive_path

	def delete_archive(archive_path: str):
		"""
		Given an archive path, deletes the archive.
		"""
		archive_path = get_archive_path(archive_path)
		remove(archive_path)

	def get_archive_time(archive_path: str):
		"""
		Given an archive path, returns the time the archive was created.
		"""
		archive_path = get_archive_path(archive_path)
		archive_time = datetime.fromtimestamp(Path(archive_path).stat().st_ctime)
		return archive_time

	def get_archive_size(archive_path: str):
		"""
		Given an archive path, returns the size of the archive.
		"""
		archive_path = get_archive_path(archive_path)
		archive_size = Path(archive_path).stat().st_size
		return archive_size

	def get_archive_date(archive_path: str):
		"""
		Given an archive path, returns the date the archive was created.
		"""
		archive_path = get_archive_path(archive_path)
		archive_date = datetime.fromtimestamp(Path(archive_path).stat().st_ctime)
		return archive_date

	def get_archive_last_modified(archive_path: str):
		"""
		Given an archive path, returns the last modified time of the archive.
		"""
		archive_path = get_archive