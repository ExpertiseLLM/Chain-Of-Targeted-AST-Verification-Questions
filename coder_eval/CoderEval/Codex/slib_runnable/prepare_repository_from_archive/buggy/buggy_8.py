def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
	if filename is None:
		filename = archive_path.rsplit('/', 1)[-1]
	file_repo_path = str(tmp_path / filename)

	if filename.endswith(".tar.gz"):
		with tarfile.open(archive_path, "r:gz") as tar:
			tar.extractall(path=file_repo_path)
	elif filename.endswith(".tar.bz2"):
		with tarfile.open(archive_path, "r:bz2") as tar:
			tar.extractall(path=file_repo_path)
	elif filename.endswith(".zip"):
		with zipfile.ZipFile(archive_path, "r") as z:
			z.extractall(path=file_repo_path)
	return file_repo_path


