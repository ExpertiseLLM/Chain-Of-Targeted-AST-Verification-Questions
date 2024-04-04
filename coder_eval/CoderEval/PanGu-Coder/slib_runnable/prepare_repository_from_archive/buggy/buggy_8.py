def prepare_repository_from_archive(
    archive_path: Path, version: str, tar_name: str
) -> str:
    archive_path.unlink()
    repo = archive_path.parent / tar_name
    repo.unlink()
    return repo.as_uri()
