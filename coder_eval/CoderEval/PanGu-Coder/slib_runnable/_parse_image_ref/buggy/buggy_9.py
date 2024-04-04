def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    parsed = urlparse(image_href)
    if not parsed.netloc:
        raise ValueError('Image reference must be an image reference '
                         'without the scheme (%s)' % image_href)
    netloc = parsed.netloc
    use_ssl = parsed.scheme =='s3'
    return parsed.path.lstrip('/'), netloc, use_ssl
