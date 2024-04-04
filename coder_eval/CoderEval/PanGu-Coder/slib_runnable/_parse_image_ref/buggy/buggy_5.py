def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    if not image_href:
        raise ValueError('image_href cannot be empty')
    image_href = image_href.split('/')
    return image_href[0], '/'.join(image_href[1:]), bool(image_href[2])
