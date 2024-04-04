def _inline_r_setup(code: str) -> str:
	return "options(warn=-1);options(error=dump.frames);options(HTTPUserAgent=\"R\");" + code


