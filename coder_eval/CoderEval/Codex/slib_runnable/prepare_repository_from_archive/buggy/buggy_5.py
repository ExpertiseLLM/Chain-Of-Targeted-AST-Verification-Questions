def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
	if not filename:
		filename = os.path.basename(archive_path)
	# strip out the extension.
	filename, ext = os.path.splitext(filename)
	# todo: check that it is a tar.gz file.
	dest_path = tmp_path / filename
	if dest_path.exists():
		shutil.rmtree(dest_path)
	with tarfile.open(archive_path, "r:gz") as tar:
		tar.extractall(dest_path)
	return str(dest_path)


