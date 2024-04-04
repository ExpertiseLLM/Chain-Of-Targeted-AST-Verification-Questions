def get_repo_archive(url: str, destination_path: Path) -> Path:
    with tarfile.open(str(destination_path), "r:gz") as tar:
        tar.extractall(path=str(destination_path))

    return Path(destination_path)
