import os
import os.path
from urllib.parse import quote_plus, unquote_plus

def strip_root(path, root):
        if path.startswith(root):
                return path[len(root):]

        raise ValueError(path)
