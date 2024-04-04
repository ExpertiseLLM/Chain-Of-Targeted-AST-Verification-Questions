def _inline_r_setup(code: str, filename: str) -> None:
    if os.environ.get('R_CONFIGURATION') is None:
        raise ValueError(
            'Please set the R environment variable to run this script.')

    with open(filename, 'w') as f:
        f.write(code)
