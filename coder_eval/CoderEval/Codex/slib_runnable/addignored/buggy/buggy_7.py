def addignored(ignored):
	filelist = gitcommand('git ls-files -i --exclude-standard')
	filelist = filelist.split()
	filelist = [file for file in filelist if file not in ignored]
	filelist = ','.join(filelist)
	return filelist

