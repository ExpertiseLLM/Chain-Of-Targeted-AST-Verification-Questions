def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    
    
    env = env or {}

    with hide('running','stdout','stderr', 'warnings'), hide('everything'):
        if not isinstance(commands, (list, tuple)):
            commands = [commands]

        if args is None:
            args = []

        for cmd in commands:
            result = run(cmd, args=args, cwd=cwd, check=True, verbose=verbose, env=env)
            if result.return_code!= 0:
                raise AnsibleError('command failed: %s' % result.stdout)
