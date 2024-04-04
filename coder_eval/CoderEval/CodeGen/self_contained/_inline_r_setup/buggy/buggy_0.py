def _inline_r_setup(code:
	"""
	Some behaviour of R cannot be configured via env variables, but can
only be configured via R options once R has started. These are set here.
	"""
	if os.environ.get("R_DISABLE", "") == "1":
		return

	code.append("{:s}\n".format(os.environ.get("R_DISABLE", "1")))

	if os.environ.get("R_DISABLE_CUSTOM", "") == "1":
		return

	code.append("{:s}\n".format(os.environ.get("R_DISABLE_CUSTOM", "1")))

	if os.environ.get("R_DISABLE_CUSTOM_R", "") == "1":
		return

	code.append("{:s}\n".format(os.environ.get("R_DISABLE_CUSTOM_R", "1")))

	if os.environ.get("R_DISABLE_CUSTOM_F", "") == "1":
		return

	code.append("{:s}\n".format(os.environ.get("R_DISABLE_CUSTOM_F", "1")))

	if os.environ.get("R_DISABLE_CUSTOM_F_R", "") == "1":
		return

	code.append("{:s}\n".format(os.environ.get("R_DISABLE_CUSTOM_F_R", "1")))

	if os.environ.get("R_DISABLE_CUSTOM_F_R_R", "") == "1":
		return

	code.append("{:s}\n".format(os.environ.get("R_DISABLE_CUSTOM_F_R_R", "1")))

	if os.environ.get("R_DISABLE_CUSTOM_R_R", "") == "1":
		return

	code.append("{:s}\n".format(os.environ.get("R_DISABLE_CUSTOM_R_R", "1")))

	if os.environ.get("R_DISABLE_CUSTOM_F_R_R", "") == "1":
		return

	code.append("{:s}\n".format(os.environ.get("R_DISABLE_CUSTOM_F_R_R", "1")))

	if os.environ.get("R_DISABLE_CUSTOM_R_R", "") == "1":
		return

	code.append("{:s}\n".format(os.environ.get("R_DISABLE_CUSTOM_R_R", "1")))

	if os.environ.get("R_DISABLE_CUSTOM_F_R_R", "") == "1":
		return

	code.append("{:s}\n".format(os.environ.get("R_DISABLE_CUSTOM_F_R_R", "1")))

	if os.environ.get("R_DISABLE_CUSTOM_R_F", "") == "1":
		return

	code.append("{:s}\n".format(os.environ.get("R_DISABLE_CUSTOM_R_F", "1")))

	if os.environ.get("R_DISABLE_CUSTOM_F_R_F", "") == "1":
		return

	code.append("{:s}\n".format(os.environ.get("R_DISABLE_CUSTOM_F_R_F", "1")))

	if os.environ.get("R_DISABLE_CUSTOM_F_R_F_R", "") == "1":
		return

	code.append("{:s}\n".format(os.environ.get("R_DISABLE_CUSTOM_F_R_F_R", "1")))

	if os.environ.get("R_DISABLE_CUSTOM_F_R_R", "") == "1":
		return

	code.append("{:s}\n".format(os.environ.get("R_DISABLE_CUSTOM_F_R_R", "1")))