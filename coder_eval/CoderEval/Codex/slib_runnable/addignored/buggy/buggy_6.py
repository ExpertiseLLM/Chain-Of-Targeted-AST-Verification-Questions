def addignored(ignored):
	ignored = ",".join(sorted(subprocess.check_output(["git", "ls-files", "--ignored", "--exclude-standard", "--others", "--directory"]).split()))
	return ignored

