def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    if len(commands) == 0:
        return
    if len(commands) == 1:
        # Avoid stderr printing to stdout.
        commands = [commands[0]]
    for command in commands:
        run_command_no_output(command, args, cwd, verbose, hide_stderr, env)
