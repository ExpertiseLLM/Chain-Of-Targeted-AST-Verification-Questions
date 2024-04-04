def get_repo_archive(url: str, destination_path: Path) -> Path:
	path = destination_path / url.split('/')[-1]
	if path.exists():
		return path

	logger.info('Downloading .tar.gz archive from "%s"', url)
	response = requests.get(url, stream=True)
	with tempfile.TemporaryDirectory() as temp_dir:
		temp_path = Path(temp_dir) / url.split('/')[-1]
		with temp_path.open('wb') as temp_file:
			for chunk in response.iter_content(chunk_size=chunk_size):
				if chunk:
					temp_file.write(chunk)

		with tarfile.open(temp_path) as tar:
			tar.extractall(destination_path)

	return path


