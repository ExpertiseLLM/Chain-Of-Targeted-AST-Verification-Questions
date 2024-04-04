def addignored(ignored):
    cmd = ['git', 'ls-files']
    output = subprocess.check_output(cmd, universal_newlines=True)
    output = output.split('\n')
    output.sort()
    return ','.join(output)
