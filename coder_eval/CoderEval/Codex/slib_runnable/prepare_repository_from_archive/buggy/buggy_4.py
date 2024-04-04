def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
	if not filename:
		filename = os.path.basename(archive_path)
	tmp_path = Path(tmp_path)
	tmp_path.mkdir(exist_ok=True)
	tmp_path = tmp_path / filename
	# open the archive, read its contents
	with open(archive_path, "rb") as archive:
		# write the contents to the temp path
		with open(tmp_path, "wb") as tmp_file:
			shutil.copyfileobj(archive, tmp_file)
	# extract the archive to the specified path
	with tarfile.open(tmp_path, "r:*") as tf:
		tf.extractall(path=tmp_path.parent)
	# return the extracted path
	return str(tmp_path.parent)


