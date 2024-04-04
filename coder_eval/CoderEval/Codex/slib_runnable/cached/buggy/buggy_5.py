def cached(cache, key=hashkey, lock=None):
	def decorating_function(user_function):
		if lock is None:
			lock = threading.Lock()
		def wrapper(*args, **kwds):
			store = cache
			try:
				key_ = key(*args, **kwds)
			except TypeError:
				# uncachable -- for instance, passing a list as an argument.
				# Better to not cache than to blow up entirely.
				return user_function(*args, **kwds)
			try:
				lock.acquire()
				try:
					return store[key_]
				except KeyError:
					pass
			finally:
				lock.release()
			result = user_function(*args, **kwds)
			try:
				lock.acquire()
				try:
					store[key_] = result
				except TypeError
