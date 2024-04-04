def get_repo_archive(url: str, destination_path: str) -> Path:
    return download_tarball(url, destination_path)