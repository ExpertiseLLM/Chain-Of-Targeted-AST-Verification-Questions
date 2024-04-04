def get_repo_archive(url: str, destination_path: Path) -> Path:

    """Given an url and a destination path, retrieve and extract .tar.gz archive
which contains 'desc' file for each package.
Each .tar.gz archive corresponds to an Arch Linux repo ('core', 'extra', 'community').

Args:
    url: url of the .tar.gz archive to download
    destination_path: the path on disk where to extract archive

Returns:
    a directory Path where the archive has been extracted to."""
    r = requests.get(url, stream=True)
    for i, repo in enumerate(r.iter_content(1024)):
        if i % 100 == 0:
            logger.info(f"Processed {i} of {len(r.iter_content(1024))} repo archives")
        with destination_path.open("wb") as f:
            f.write(repo)
    return destination_path
