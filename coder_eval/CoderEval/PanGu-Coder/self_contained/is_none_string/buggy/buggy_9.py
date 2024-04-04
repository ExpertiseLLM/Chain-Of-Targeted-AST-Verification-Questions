def is_none_string(val: str) -> bool:
    return val.lower() in ("none", "none or empty", "none or empty or empty")
