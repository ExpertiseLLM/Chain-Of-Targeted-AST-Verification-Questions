def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    
    
    if not env:
        env = os.environ.copy()

    if cwd:
        env['PWD'] = cwd

    return subprocess.call(commands, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd, verbose=verbose)