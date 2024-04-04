def get_repo_archive(url: str, destination_path: str) -> Path:
    archive = urllib.request.urlopen(url)
    with tarfile.open(fileobj=archive) as tar:
        tar.extractall(destination_path)
    return Path(destination_path)
