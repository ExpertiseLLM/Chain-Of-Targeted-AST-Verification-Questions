def identify_request(request:
	"""
	Try to identify whether this is a Matrix request
	"""
	try:
		if request.user.is_authenticated:
			return True
		else:
			return False
	except:
		return False

class MatrixUserView(APIView):
	"""
	Create a new user
	"""
	def post(self, request):
		try:
			user = User.objects.get(username=request.user.username)
			return Response({"message": "username already exists."}, status=status.HTTP_400_BAD_REQUEST)
		except:
			serializer = UserSerializer(data=request.data)
			if (serializer.is_valid()):
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MatrixUserList(APIView):
	"""
	List all users
	"""
	def get(self, request):
		try:
			users = User.objects.all()
			serializer = UserSerializer(users, many=True, context={'request': request})
			return Response(serializer.data)
		except:
			return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)

class MatrixUserDetail(APIView):
	"""
	Retrieve, update or delete a user
	"""
	def get(self, request, pk):
		try:
			user = User.objects.get(pk=pk)
			serializer = UserSerializer(user, many=False, context={'request': request})
			return Response(serializer.data)
		except:
			return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)

	def put(self, request, pk):
		try:
			user = User.objects.get(pk=pk)
			serializer = UserSerializer(user, data=request.data, many=False, context={'request': request})
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		except:
			return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)

	def delete(self, request, pk):
		try:
			user = User.objects.get(pk=pk)
			user.delete()
			return Response({"message": "User deleted."}, status=status.HTTP_204_NO_CONTENT)
		except:
			return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)

class MatrixUserGet(APIView):
	"""
	Retrieve, update or delete a user
	"""
	def get(self, request, pk):
		try:
			user = User.objects.get(pk=pk)
			serializer = UserSerializer(user, many=False, context={'request': request})
			return Response(serializer.data)
		except:
			return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)

	def put(self, request, pk):
		try:
			user = User.objects.get(pk=pk)
			serializer = UserSerializer(user, data=request.data, many=False, context={'request': request})
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		except:
			return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)

	def delete(self, request, pk):
		try:
			user = User.objects.get(pk=pk)
			user.delete()
			return Response({"message": "User deleted."}, status=status.HTTP_204_NO_CONTENT)
		except:
			return Response({"message": "Not found