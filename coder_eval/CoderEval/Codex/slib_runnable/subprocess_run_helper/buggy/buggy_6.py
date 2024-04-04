def subprocess_run_helper(func, *args, timeout, extra_env=None):
	if 'win' in sys.platform:
		kwargs = {
			'creationflags': subprocess.CREATE_NEW_PROCESS_GROUP,
			'close_fds': True,
			'env': os.environ.copy()
		}
	else:
		kwargs = {
			'preexec_fn': os.setsid,
			'close_fds': True,
			'env': os.environ.copy()
		}

	if extra_env is not None:
		kwargs['env'].update(extra_env)

	if timeout > 0:
		# Create a thread that will raise an exception in the main thread
		# after timeout seconds.
		thread = threading.Thread(target=thread_helper, args=(timeout,))
		thread.start()

		try:
			subprocess.run([sys.executable, '-c',
							compile('import sys; from {module} import {function};
