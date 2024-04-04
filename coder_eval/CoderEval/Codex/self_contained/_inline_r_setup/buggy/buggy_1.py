def _inline_r_setup(code: str) -> str:
	if os.environ.get("R_ENABLE_JIT", "false") == "true":
		code = f"""
			rpy2.robjects.r(\"options(rpy2.enable_on_demand=TRUE)\")
			rpy2.robjects.r(\"options(rpy2.enable_jit=TRUE)\")
			""" + code
	return code


