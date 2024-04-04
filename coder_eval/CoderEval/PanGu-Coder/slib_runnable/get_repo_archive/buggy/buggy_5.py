def get_repo_archive(url: str, destination_path: Path) -> Path:
    tarball_name = url.split("/")[-1]
    return download_tarball(url, destination_path, tarball_name)
