from rest_framework.response import Response
from login.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token

from rest_framework import status
from login import models
from rest_framework.views import APIView
from django.contrib.auth.models import User

from django.contrib.auth.hashers import check_password

from posts.api.permissions import PostWriterOrAdminOrReadOnly


class UserCountView(APIView):
	def post(self, request):

		try:
			users = User.objects.all().count()
			return Response({'users' : users}, status=status.HTTP_200_OK)
		except:
			return Response({"detail" : "Users not found"}, status=status.HTTP_400_BAD_REQUEST)
			

class registration_request(APIView):

	def post(self, request):
		serializer = RegistrationSerializer(data=request.data)


		if serializer.is_valid():
			print("we have the new user object")
			account = serializer.save()
			data = serializer.data
			data['user'] = data['username']

			token = Token.objects.get(user=account).key
			data['token'] = token
			data['is_first_time'] = True

			return Response(data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class login_view(APIView):
	def post(self, request):

		# json.loads(request.body.decode('utf-8'))
		try:
			username = request.data.get('username')
			password = request.data.get('password')
		except:
			return Response({'detail' : 'could not read data'}, status=status.HTTP_404_NOT_FOUND)


		try:
			user_object = User.objects.get(username=username)
		except:
			return Response({"detail" : "username is wrong"}, status=status.HTTP_400_BAD_REQUEST)
		
		if check_password(password, user_object.password):
			try:
				Token.objects.get_or_create(user=user_object)
				token = Token.objects.get(user=user_object).key

				data = {}
				data['token'] = token
				data['user'] = user_object.username

				return Response(data, status=status.HTTP_200_OK)			
			except:
				return Response({'detail' : 'login failed'}, status=status.HTTP_409_CONFLICT)
		else:
			return Response({"detail" : "password is wrong"}, status=status.HTTP_401_UNAUTHORIZED)


class logout_view(APIView):

	def post(self, request):
		request.user.auth_token.delete()

		return Response({"detail" : "logout done"}, status=status.HTTP_200_OK)
