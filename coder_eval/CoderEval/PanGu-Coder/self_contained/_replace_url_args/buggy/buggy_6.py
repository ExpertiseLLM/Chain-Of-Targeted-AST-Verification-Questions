def _replace_url_args(url, url_args):
    for k, v in url_args.items():
        if isinstance(v, str):
            url = url.replace("{" + k + "}", v)
        else:
            url = url.replace("{" + k + "}", str(v))
    return url
