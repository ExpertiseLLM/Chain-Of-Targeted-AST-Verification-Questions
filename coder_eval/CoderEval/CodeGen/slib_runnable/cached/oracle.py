from curses import has_key
import functools


def cached(cache, key=has_key, lock=None):
    """Decorator to wrap a function with a memoizing callable that saves
    results in a cache.

    """
    def decorator(func):
        if cache is None:
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
        elif lock is None:
            def wrapper(*args, **kwargs):
                k = key(*args, **kwargs)
                try:
                    return cache[k]
                except KeyError:
                    pass  # key not found
                v = func(*args, **kwargs)
                try:
                    cache[k] = v
                except ValueError:
                    pass  # value too large
                return v
        else:
            def wrapper(*args, **kwargs):
                k = key(*args, **kwargs)
                try:
                    with lock:
                        return cache[k]
                except KeyError:
                    pass  # key not found
                v = func(*args, **kwargs)
                # in case of a race, prefer the item already in the cache
                try:
                    with lock:
                        return cache.setdefault(k, v)
                except ValueError:
                    return v  # value too large
        return functools.update_wrapper(wrapper, func)
    return decorator
