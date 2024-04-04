def get_repo_archive(url: str, destination_path: str) -> Path:
    archive_path = pathlib.Path(destination_path)

    if not archive_path.exists():
        tarball = tarfile.open(url, "r:gz")
        tarball.extractall(path=destination_path)
        tarball.close()

    return archive_path
