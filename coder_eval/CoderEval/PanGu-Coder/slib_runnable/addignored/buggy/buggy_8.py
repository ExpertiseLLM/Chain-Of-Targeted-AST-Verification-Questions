def addignored(ignored):
    # define the command to be used
    command = "git ls-files -z --ignore-standard --others --exclude-standard.git"
    # run it
    output = subprocess.check_output(command, shell=True)
    # extract the filenames
    filenames = output.decode("utf-8").split('\n')
    # sort the list of filenames to make sure we only return the files in the ignored directory
    filenames.sort()
    # return the string representation of the files
    return ', '.join(filenames)