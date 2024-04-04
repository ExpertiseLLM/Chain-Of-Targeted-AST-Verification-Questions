def prepare_repository_from_archive(
    archive_path: str,
    filename: Optional[str] = None,
    tmp_path: Union[PosixPath, str] = "/tmp",
) -> str:
	filename = filename or path.basename(archive_path)

	# If the file is gzipped, uncompress it.
	if filename.endswith(".gz"):
		with gzip.open(archive_path, "rb") as gzipped:
			with tempfile.NamedTemporaryFile(delete=False, dir=tmp_path, suffix=".tar") as tmp:
				# Copy the contents of the gzipped file into the temporary file.
				copyfileobj(gzipped, tmp)
				tmp_archive_path = tmp.name
	else:
		tmp_archive_path = archive_path

	repo_path = path.join(tmp_path, "repo")
	with tarfile.open(tmp_archive_path) as tar:
		tar.extractall(path=repo_path)
		tar.close()
	os.remove(tmp_archive_path)
	return repo_path


