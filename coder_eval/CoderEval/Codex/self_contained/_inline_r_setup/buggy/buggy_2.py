def _inline_r_setup(code: str) -> str:
	return (
		"options(max.print=1e9, width=1e9); " +
		code
	)

