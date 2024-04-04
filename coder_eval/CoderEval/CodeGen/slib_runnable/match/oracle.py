import os
def match(filename):
    """
    Check if the filename is a type that this module supports

    Args:
        filename: Filename to match
    Returns:
        False if not a match, True if supported
    """

    base_name = os.path.basename(filename)
    base_name_lower = base_name.lower()
    return base_name_lower == 'doxyfile'
