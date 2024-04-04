def match_file_by_prefix(prefix, file_path):
	return (
		file_path.name.startswith(prefix)
		and (
			file_path.suffix in (".xml", ".pdf", ".txt", ".doc", ".docx", ".odt")
		)
		and (file_path.name != "mets.xml")
	)


