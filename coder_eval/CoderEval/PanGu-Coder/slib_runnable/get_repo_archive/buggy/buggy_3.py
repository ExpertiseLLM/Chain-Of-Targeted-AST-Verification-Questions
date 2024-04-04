def get_repo_archive(url: str, destination_path: Path) -> Path:
    archive_path = destination_path / Path("desc")
    if not archive_path.exists():
        _download_tarball(url, destination_path)
    return archive_path
