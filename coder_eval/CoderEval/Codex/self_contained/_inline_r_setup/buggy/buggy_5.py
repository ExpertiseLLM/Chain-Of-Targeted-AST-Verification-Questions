def _inline_r_setup(code: str) -> str:
	return (
		f"options(unzip = '{_unzip_path()}')\n"
		f"options(browser = '{_browser_path()}')\n"
		f'options(repos = c(CRAN = "{r_cran_repository}",\n'
		f'                 BioC = "{r_bioc_repository}"))\n'
		+ code
	)


