def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    image_id = _image_id_from_href(image_href)
    netloc = _netloc_from_href(image_href)
    use_ssl = _is_true(image_href.find('https://'))
    return image_id, netloc, use_ssl
