def _inline_r_setup(code: str):
    global _inline_r_config
    _inline_r_config = _inline_r_config or R.load_config()
    if _inline_r_config is None:
        raise Exception(f"R is not configured correctly. In order to set R options, you must run `rm -rf` first. Check the installation of R.")
    if "R_TEST_ENV_VARIABLE" in os.environ:
        raise Exception(f"R is configured as a test environment. This is not allowed in production.")
