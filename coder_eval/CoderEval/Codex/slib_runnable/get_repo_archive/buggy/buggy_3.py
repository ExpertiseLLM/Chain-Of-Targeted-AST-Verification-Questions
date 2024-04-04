def get_repo_archive(url: str, destination_path: Path) -> Path:
	logger.info(f'Downloading repo archive from {url}')
	try:
		tmp_path = download_and_extract(url, destination_path)
	except Exception as e:
		logger.error(e)
		return None
	return tmp_path


