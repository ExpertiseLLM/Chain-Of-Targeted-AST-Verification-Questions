def prepare_repository_from_archive(
    archive_path: Path, repo_name: str, worktree: str = ""
) -> str:
    with archive_path.open("rb") as archive:
        archive_content = archive.read()

    repo_url = get_repository_url_from_content(archive_content, repo_name, worktree)
    return repo_url
