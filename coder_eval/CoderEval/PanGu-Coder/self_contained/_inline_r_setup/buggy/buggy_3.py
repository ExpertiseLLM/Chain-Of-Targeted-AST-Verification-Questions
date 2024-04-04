def _inline_r_setup(code: str):
    # Set up environment variables and inline R
    _inline_r_env_setup(code)
    # Set up R environment variables that are not configured via R
    _inline_r_env_setup_non_existent_vars(code)
