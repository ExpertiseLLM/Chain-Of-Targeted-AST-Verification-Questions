def get_repo_archive(url: str, destination_path: Path) -> Path:
	archive_path = destination_path / url.split('/')[-1]
	if not archive_path.exists():
		print(f"Downloading {url} ...")
		download(url, archive_path)
	else:
		print(f"{archive_path} already exists, skipping download.")

	print(f"Extracting {archive_path} ...")
	with tarfile.open(archive_path) as tf:
		tf.extractall(destination_path)

	return destination_path / 'desc'


