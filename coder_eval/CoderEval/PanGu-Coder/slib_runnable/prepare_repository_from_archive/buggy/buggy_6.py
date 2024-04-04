def prepare_repository_from_archive(
    archive_path: str, dest_path: str, strip_path_prefix: bool = True
) -> str:
    with archive_path.open("rb") as f:
        return _prepare_repository_from_archive(
            f, dest_path, strip_path_prefix
        )
