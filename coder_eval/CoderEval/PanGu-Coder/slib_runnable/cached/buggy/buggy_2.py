def cached(cache, key=hashkey, lock=None):
    if lock is None:
        lock = Lock()

    def wrapper(func):
        def wrapped(*args, **kwargs):
            key = key(*args, **kwargs)
            result = cache.get(key)
            if result is None:
                result = func(*args, **kwargs)
                cache.set(key, result)
            return result
        return wrapped
    return wrapper