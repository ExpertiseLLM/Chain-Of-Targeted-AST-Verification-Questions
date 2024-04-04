def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    if not isinstance(commands, list):
        commands = [commands]

    if cwd is None:
        cwd = os.getcwd()

    for command in commands:
        if verbose:
            print("Running command: %s" % command)
        subprocess.call(command, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
