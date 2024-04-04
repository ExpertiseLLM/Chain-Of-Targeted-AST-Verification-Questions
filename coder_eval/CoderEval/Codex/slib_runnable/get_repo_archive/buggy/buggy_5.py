def get_repo_archive(url: str, destination_path: Path) -> Path:
	logger.info(f'Downloading repo archive: {url}')
	# Download
	archive_path = destination_path / url.split('/')[-1]
	if archive_path.exists():
		logger.info(f'Archive already exists: {archive_path}')
	else:
		try:
			with archive_path.open(mode='wb') as f:
				f.write(requests.get(url).content)
		except Exception as e:
			raise e
	logger.info(f'Extracting archive: "{archive_path}" in "{destination_path}"')
	# Extract
	extracted_path = destination_path / archive_path.stem
	if extracted_path.exists():
		logger.info(f'Archive already extracted: {extracted_path}')
	else:
		try:
			with tarfile.open(archive_path) as f:
				f.extractall(str(destination_path))
		
