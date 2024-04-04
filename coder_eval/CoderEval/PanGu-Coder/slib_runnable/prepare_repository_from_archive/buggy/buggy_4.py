def prepare_repository_from_archive(
    archive_path: str, archive_url: str, prefix: str
) -> str:
    with tarfile.open(archive_path) as archive:
        archive.extractall(path=archive_url)
    return archive_url + prefix + archive_path.split(archive_path)[-1]
