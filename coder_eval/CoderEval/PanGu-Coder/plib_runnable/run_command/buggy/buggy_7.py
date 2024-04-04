def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    
    
    for command in commands:
        if isinstance(command, str):
            command = command.split()
        args = command + args
        run(args, cwd=cwd, verbose=verbose, hide_stderr=hide_stderr, env=env)