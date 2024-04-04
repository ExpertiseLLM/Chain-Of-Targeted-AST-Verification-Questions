def get_repo_archive(url: str, destination_path: Path) -> Path:
	log.info(f"Downloading '{url}' to '{destination_path}'")
	with requests.get(url, stream=True) as r:
		r.raise_for_status()
		with tarfile.open(fileobj=io.BytesIO(r.content), mode="r:gz") as tar:
			tar.extractall(destination_path)
			return destination_path


