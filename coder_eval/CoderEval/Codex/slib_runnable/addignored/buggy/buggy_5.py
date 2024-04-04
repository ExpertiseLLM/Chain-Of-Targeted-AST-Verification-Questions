def addignored(ignored):
	# Get the list of files from the git status command
	output = subprocess.check_output(["git", "status", "--porcelain"]).decode()
	# Turn the output into a list
	output = output.split("\n")
	# Remove any empty elements in the list
	output = list(filter(None, output))
	# Remove any elements that are not ignored
	output = [i for i in output if i.startswith("!!")]
	# Remove the leading "!!"
	output = [i[2:] for i in output]
	# Remove any elements that are directories
	output = [i for i in output if os.path.isfile(i)]
	# If the list is not empty
	if output:
		# Join the list with commas
		output = ",".join(output)
		# Append the ignored list to the existing ignored list
		ignored = ignored + "," + output
		# Return the ignored list
		return ignored
	# Otherwise
	else:
		# Return the ignored list
		return ignored
