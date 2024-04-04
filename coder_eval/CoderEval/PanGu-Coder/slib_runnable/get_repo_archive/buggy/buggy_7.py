def get_repo_archive(url: str, destination_path: str) -> Path:
    archive_path = Path(destination_path) / Path(url.split('/')[-1]).split('.')[0] / 'desc.tar.gz'
    archive_path.unlink()
    extract_tarball(url, archive_path)
    return archive_path
