def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
	if not filename:
		filename = archive_path.split("/")[-1]

	if isinstance(tmp_path, str):
		tmp_path = Path(tmp_path)

	tmp_path = tmp_path / filename.split(".")[0]
	tmp_path.mkdir(exist_ok=True)

	if not tmp_path.exists():
		raise ValueError(f"{tmp_path} does not exist")

	with TemporaryDirectory(dir=tmp_path) as dir_path:
		with zipfile.ZipFile(archive_path, "r") as zip_ref:
			zip_ref.extractall(dir_path)

			return f"file://{dir_path}"

