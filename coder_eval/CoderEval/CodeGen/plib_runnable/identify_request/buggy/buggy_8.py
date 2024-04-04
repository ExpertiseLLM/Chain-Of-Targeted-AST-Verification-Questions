def identify_request(request:
	"""
	Try to identify whether this is a Matrix request
	"""
	try:
		input_matrix = request.GET['matrix']

		return input_matrix
	except KeyError:
		raise Http404
	except:
		return "Please enter a matrix or a matrix file"

