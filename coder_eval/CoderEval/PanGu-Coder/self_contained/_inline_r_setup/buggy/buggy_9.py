def _inline_r_setup(code: str) -> str:
    return """
# R is still configured via env variables. This should be set by R only.
# R should not be configured via R options anymore.

export R_LOG_LEVEL=INFO

export R_LOG_FILE=/dev/null

export R_LOG_LEVEL_DETAILS=true
"""
