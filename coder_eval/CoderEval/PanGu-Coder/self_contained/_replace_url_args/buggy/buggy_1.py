def _replace_url_args(url, url_args):
    for key, value in url_args.iteritems():
        url = url.replace('{' + key + '}', value)
    return url
