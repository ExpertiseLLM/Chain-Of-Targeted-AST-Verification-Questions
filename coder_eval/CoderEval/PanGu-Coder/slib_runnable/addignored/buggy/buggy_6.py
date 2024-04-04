def addignored(ignored):

    if ignored == []:
        return ''

    ignored = ', '.join(sorted(ignored))

    return '\n'.join([
        '[Ignored]',
        '',
       '   {0}'.format(ignored)
    ])