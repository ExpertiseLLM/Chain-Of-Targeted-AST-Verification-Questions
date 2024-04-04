def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
	if not filename:
		filename = os.path.basename(archive_path)
	tmp_dir = tmp_path + "/" + filename.split(".")[0] + "-" + str(uuid.uuid1())[:8]
	os.makedirs(tmp_dir, exist_ok=True)
	with zipfile.ZipFile(archive_path, "r") as zip_ref:
		zip_ref.extractall(tmp_dir)
	return "file://" + tmp_dir


