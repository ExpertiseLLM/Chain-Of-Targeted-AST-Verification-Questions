def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    
    
    if isinstance(commands, str):
        commands = [commands]
    for command in commands:
        run_command_impl(command, args, cwd, verbose, hide_stderr, env)
