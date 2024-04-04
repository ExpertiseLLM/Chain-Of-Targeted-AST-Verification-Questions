def _inline_r_setup(code: str) -> str:
	return (
		f"""
		options(
			max.print = 9999999,
			warn = -1
		)
		{code}
		"""
	)


