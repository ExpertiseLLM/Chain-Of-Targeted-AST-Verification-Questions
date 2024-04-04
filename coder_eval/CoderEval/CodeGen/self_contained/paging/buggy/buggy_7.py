def paging(response, max_results):
	"""
	Returns WAPI response page by page

Args:
    response (list): WAPI response.
    max_results (int): Maximum number of objects to be returned in one page.
Returns:
    Generator object with WAPI response split page by page.
	"""
	for i in range(0, int(max_results)):
		yield response
		response = response.next()
	return response
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime

from. import config