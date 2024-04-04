def oneline(script, seperator=" && "):
    return seperator.join([shlex.quote(x) for x in script.split("\n")])
