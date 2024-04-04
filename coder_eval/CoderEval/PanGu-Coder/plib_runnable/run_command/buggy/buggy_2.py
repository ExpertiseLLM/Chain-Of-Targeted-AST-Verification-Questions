def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    if not env:
        env = {}
    if verbose:
        env['PYTHON_VERBOSE'] = '1'
    if hide_stderr:
        env['PYTHON_SHOW_STDERR'] = '1'
    if isinstance(commands, six.string_types):
        commands = [commands]
    for command in commands:
        subprocess.check_call(command, env=env, cwd=cwd, stdout=subprocess.DEVNULL,
                              stderr=subprocess.DEVNULL)
