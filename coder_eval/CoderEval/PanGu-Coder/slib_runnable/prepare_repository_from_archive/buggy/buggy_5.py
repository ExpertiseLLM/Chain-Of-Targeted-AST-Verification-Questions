def prepare_repository_from_archive(
    archive_path: str,
    repo_name: str,
    repo_url: str,
    target_dir: str,
) -> str:
    archive_repo_url = get_archive_repository_url(archive_path, repo_name)
    return prepare_repository_from_repository_url(archive_repo_url, repo_name, repo_url, target_dir)
