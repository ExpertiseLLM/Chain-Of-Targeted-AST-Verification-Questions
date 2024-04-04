def prepare_repository_from_archive(
    archive_path: str, repository_url: str
) -> str:
    if archive_path is None:
        return repository_url
    return _uncompress_archive(archive_path, repository_url)
