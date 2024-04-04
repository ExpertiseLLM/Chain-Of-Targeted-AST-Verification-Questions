def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    if not isinstance(commands, list):
        commands = [commands]
    for command in commands:
        _run_command(command, args, cwd, verbose, hide_stderr, env)