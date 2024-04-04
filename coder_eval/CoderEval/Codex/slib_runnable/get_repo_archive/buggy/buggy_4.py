def get_repo_archive(url: str, destination_path: Path) -> Path:
	destination_path.mkdir(exist_ok=True)
	if not destination_path.is_dir():
		raise ValueError(f'{destination_path} is not a directory')

	# Download archive
	tar_gz_archive_name = url.split('/')[-1]
	tar_gz_archive_path = destination_path / tar_gz_archive_name
	if not tar_gz_archive_path.exists():
		download(url, tar_gz_archive_path)
	if not tar_gz_archive_path.is_file():
		raise ValueError(f'{tar_gz_archive_path} is not a file')

	# Extract archive
	tar_file_name = tar_gz_archive_name.replace('.gz', '')
	tar_file_path = destination_path / tar_file_name
	if not tar_file_path.exists():
		with gzip.open(tar_gz_archive_path, 'rb') as f_in, open(tar_file_path, 'wb') as
