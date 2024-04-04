def addignored(ignored):
	filelist = subprocess.check_output(["git", "ls-files", "--others", "--exclude-standard"]).decode('utf-8')
	filelist = filelist.split('\n')
	filelist = [x for x in filelist if x.endswith(ignored)]
	return ','.join(filelist)

