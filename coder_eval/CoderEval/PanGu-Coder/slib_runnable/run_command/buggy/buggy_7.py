def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    if isinstance(commands, basestring):
        commands = [commands]
    return run_command_generic(commands, args, cwd, verbose, hide_stderr, env)