def get_repo_archive(url: str, destination_path: Path) -> Path:
	logger.debug('get_repo_archive(%s)', url)
	destination_path.mkdir(parents=True, exist_ok=True)
	r = requests.get(url)
	if r.status_code != 200:
		raise ValueError(f'status code is {r.status_code}')
	with tarfile.open(fileobj=io.BytesIO(r.content)) as tar:
		tar.extractall(destination_path)
	return destination_path


