def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    try:
        image_id = urlparse.urlparse(image_href).path.strip("/")
    except ValueError:
        raise ValueError(_("Invalid image reference %s") % image_href)

    netloc = urlparse.urlparse(image_href).netloc
    use_ssl = False if netloc.startswith("http") else True

    return image_id, netloc, use_ssl
