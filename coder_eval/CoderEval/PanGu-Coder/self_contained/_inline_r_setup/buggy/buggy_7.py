def _inline_r_setup(code: str, options: Optional[str] = None) -> None:
    if not options:
        options = ''
    code = code.format(options=options)
    return _run_inline(code)
