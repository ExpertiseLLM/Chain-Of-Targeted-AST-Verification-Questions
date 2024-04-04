def _inline_r_setup(code: str) -> str:
	return f"""options(width={R_TERM_WIDTH-1})
