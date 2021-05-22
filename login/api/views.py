from rest_framework.response import Response
from login.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token

from rest_framework import status
from login import models
from rest_framework.views import APIView


class registration_request(APIView):

	def post(self, request):
		serializer = RegistrationSerializer(data=request.data)


		if serializer.is_valid():
			print("we have the new user object")
			account = serializer.save()
			data = serializer.data

			token = Token.objects.get(user=account).key
			data['token'] = token

			return Response(data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class logout_view(APIView):

	def post(self, request):
		request.user.auth_token.delete()

		return Response({"detail" : "logout done"}, status=status.HTTP_200_OK)
