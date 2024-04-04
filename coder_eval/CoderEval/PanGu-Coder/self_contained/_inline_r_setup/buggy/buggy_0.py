def _inline_r_setup(code: str) -> str:
    if "R" not in os.environ:
        raise RuntimeError("Cannot set R to run R commands without previous R environment set.")
    return code
