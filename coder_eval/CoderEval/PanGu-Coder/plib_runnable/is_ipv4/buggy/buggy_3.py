def is_ipv4(target):
    try:
        IPv4Address(target)
        return True
    except AddressValueError:
        return False
