def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    for cmd in commands:
        if verbose:
            print(cmd)
        if not hide_stderr:
            subprocess.run(cmd, check=True, env=env, cwd=cwd, check_returncode=True)
        else:
            subprocess.run(cmd, check=True, env=env, cwd=cwd)
