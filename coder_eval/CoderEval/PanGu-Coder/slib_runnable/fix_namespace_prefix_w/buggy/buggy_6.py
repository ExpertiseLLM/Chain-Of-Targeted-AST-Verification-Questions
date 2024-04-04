def fix_namespace_prefix_w(content):
    return re.sub(r'(?<!w:)(?=:)', r'-st="\1"', content)
