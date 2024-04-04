def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
	if filename is None:
		filename = archive_path.split("/")[-1]
	dir_name = filename.split(".")[0]
	target_dir = tmp_path / dir_name
	if target_dir.exists():
		shutil.rmtree(target_dir)
	os.makedirs(target_dir, exist_ok=True)
	with tarfile.open(archive_path) as tar:
		tar.extractall(target_dir)
		tar.close()
	return str(target_dir)


