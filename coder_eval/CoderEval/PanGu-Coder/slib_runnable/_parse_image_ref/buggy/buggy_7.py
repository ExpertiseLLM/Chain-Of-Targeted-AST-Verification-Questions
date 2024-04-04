def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    image_id = urllib.parse.urlparse(image_href).netloc
    netloc = urllib.parse.urlparse(image_href).netloc
    use_ssl = image_href.startswith('https://')
    return image_id, netloc, use_ssl
