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
	archive = tarfile.open(url, mode="r:gz")
	archive.extractall(destination_path)
	archive.close()
	return destination_path

class RepoArchive:
	def __init__(self, url: str, destination_path: Path) -> None:
		self.url = url
		self.destination_path = destination_path
	
	def get_repo_archive(self):
		return self.destination_path

