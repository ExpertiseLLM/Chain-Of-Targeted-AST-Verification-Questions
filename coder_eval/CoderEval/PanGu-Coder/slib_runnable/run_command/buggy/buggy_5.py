def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    
    
    if not commands:
        return []
    if isinstance(commands, str):
        commands = [commands]
    if isinstance(args, str):
        args = [args]
    return subprocess.check_output(
        commands, stderr=subprocess.STDOUT, cwd=cwd, env=env, verbose=verbose, hide_stderr=hide_stderr
    )
