def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    netloc = urlparse(image_href).netloc
    image_id = urlparse(image_href).path.split('/')[-1]

    return image_id, netloc, False
