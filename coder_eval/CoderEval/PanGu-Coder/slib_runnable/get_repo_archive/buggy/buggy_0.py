def get_repo_archive(url: str, destination_path: Path) -> Path:
    if url.endswith('.tar.gz'):
        return get_repo_archive_tar(url, destination_path)
    return get_repo_archive_tar(url, destination_path)
