def _inline_r_setup(code: str):
    with open('./.env', 'w') as f:
        f.write(code)
    with open('./.r-config', 'w') as f:
        f.write(code)
