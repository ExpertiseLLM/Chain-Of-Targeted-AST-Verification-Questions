def _replace_url_args(url, url_args):
    for k, v in url_args.items():
        url = url.replace("{{{}}}".format(k), str(v))
    return url
