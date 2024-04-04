def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    if isinstance(commands, basestring):
        commands = [commands]

    with _build_log(verbose, hide_stderr) as log:
        for cmd in commands:
            cmd = cmd.format(**env)
            _run_command(cmd, args, cwd, log, verbose, hide_stderr)
