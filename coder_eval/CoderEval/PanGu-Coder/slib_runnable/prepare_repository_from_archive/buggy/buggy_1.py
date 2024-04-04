def prepare_repository_from_archive(
    archive_path: Path, verbose: bool = False
) -> Tuple[str, str]:
    return (
        archive_path.name,
        archive_path.parent / archive_path.name,
    )
