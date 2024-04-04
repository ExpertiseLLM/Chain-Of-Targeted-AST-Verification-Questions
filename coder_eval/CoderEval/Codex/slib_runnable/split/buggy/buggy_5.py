def split(s, platform='this'):
	# This is a wrapper for shlex.split() that works for
	# Windows and POSIX, with the same semantics.
	# It is a faster version of split_argv.py
	# (using regular expressions instead of shlex)
	#
	# From https://github.com/pytoolz/toolz/blob/master/toolz/curried/os.py
	# Copyright (c) 2012, Matthew Rocklin and contributors
	# All rights reserved.
	#
	# Redistribution and use in source and binary forms, with or without
	# modification, are permitted provided that the following conditions are
	# met:
	#
	#     * Redistributions of source code must retain the above copyright
	#       notice, this list of conditions and the following disclaimer.
	#     * Redistributions in binary form must reproduce the above
	#       copyright notice, this list of conditions and the following
	#       disclaimer in the documentation and/or other materials provided
	#       with the distribution.
	#     * Neither the name of Matthew Rocklin nor the names of other
	#       contributors
