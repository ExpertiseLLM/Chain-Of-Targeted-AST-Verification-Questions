def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    
    
    if isinstance(commands, str):
        commands = commands.split()
    for cmd in commands:
        cmd = cmd.strip()
        if verbose:
            print("Running: {}".format(cmd))
        subprocess.check_call(cmd, cwd=cwd, env=env, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    if not hide_stderr:
        sys.stderr.write("\n")
    if args is not None:
        subprocess.check_call(args, cwd=cwd, env=env, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
