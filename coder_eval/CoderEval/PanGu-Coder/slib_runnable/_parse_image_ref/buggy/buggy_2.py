def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    image_id = _parse_href(image_href)
    netloc = _parse_netloc(image_href)
    use_ssl = bool(image_href.find('https://'))
    return image_id, netloc, use_ssl
