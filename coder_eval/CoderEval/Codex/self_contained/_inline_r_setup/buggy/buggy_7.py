def _inline_r_setup(code: str) -> str:
	return r"""
	options("repos" = c("http://cran.r-project.org/",
		"http://rforge.net/",
		"http://www.bioconductor.org/packages/release/bioc",
		"http://www.bioconductor.org/packages/release/data/experiment",
		"http://www.bioconductor.org/packages/3.0/data/experiment"))
	""" + code


