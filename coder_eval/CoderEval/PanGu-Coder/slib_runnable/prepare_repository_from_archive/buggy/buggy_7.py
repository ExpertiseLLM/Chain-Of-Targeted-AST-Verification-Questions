def prepare_repository_from_archive(
    archive_path: str, repository_name: str
) -> str:
    with tarfile.open(archive_path) as tar:
        tar.extractall(path=repository_name)

    return repository_name
