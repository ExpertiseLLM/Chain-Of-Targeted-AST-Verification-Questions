def get_repo_archive(url:
	"""
	Given an url and a destination path, retrieve and extract.tar.gz archive
which contains 'desc' file for each package.
Each.tar.gz archive corresponds to an Arch Linux repo ('core', 'extra', 'community').

Args:
    url: url of the.tar.gz archive to download
    destination_path: the path on disk where to extract archive

Returns:
    a directory Path where the archive has been extracted to.
	"""
	try:
		import tarfile
		extract_tar = tarfile.open("{}/{}".format(url, "desc"), 'r:gz')
	except:
		print("Error, please install Tarfile, or download it from the repository at: {}".format(url))
		exit(1)
	tar_extract = extract_tar.extractall()
	tar_extract.close()
	return tar_extract

