def get_repo_archive(url: str, destination_path: Path) -> Path:
    # TODO: Add support for other paths.
    return destination_path / f"{url.split("/")[-1]}.tar.gz"
