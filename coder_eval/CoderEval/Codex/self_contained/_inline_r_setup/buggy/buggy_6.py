def _inline_r_setup(code: str) -> str:
	if not code:
		return "options(repos = 'https://cloud.r-project.org/')\n"
	return code


