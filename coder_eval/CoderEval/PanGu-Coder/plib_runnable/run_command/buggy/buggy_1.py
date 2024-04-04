def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    
    
    if not isinstance(commands, list):
        commands = [commands]
    if args:
        args = ["--"] + args
    _run_command(commands, args, cwd, verbose, hide_stderr, env)
