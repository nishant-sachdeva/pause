from rest_framework.response import Response
from login.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token

from rest_framework import status
from login import models
from rest_framework.views import APIView
from django.contrib.auth.models import User


from posts.models import Post
from posts.api.serializers import PostSerializer
from posts.api.permissions import PostWriterOrAdminOrReadOnly

def PostListAV(APIView):
	permission_classes = [PostWriterOrAdminOrReadOnly]
	def get(self, request):

		username = request.data.get('username')

		try:
			user_object = User.objects.get(username=username)
		except:
			return Response({"detail" : "User does not exists"}, status=status.HTTP_400_BAD_REQUEST)
		
		# so we have the user, so, get all posts for the username
		

		try:
			post_list = Post.objects.get(username=user_object.pk)

			serializer = PostSerializer(post_list, many=True)

			return Response(serializer.data, status=status.HTTP_200_OK)

		except:
			return Response({"detail" : "Post not found"}, status=status.HTTP_400_BAD_REQUEST)



	def post(self, request):

		# here we have to make a new post for the user 

		username = request.data.get('username')

		try:
			user_object = User.objects.get(username=username)
		except:
			return Response({"detail" : "User does not exists"}, status=status.HTTP_400_BAD_REQUEST)
		

		serializer = PostSerializer(data = request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)

		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def PostDetailAV(APIView):
	permission_classes = [PostWriterOrAdminOrReadOnly]

	def get(self,request):
		username = request.data.get('username')
		post_id  = request.data.get('post_id')
		
		try:
			user_object = User.objects.get(username=username)
		except:
			return Response({"detail" : "User does not exists"}, status=status.HTTP_400_BAD_REQUEST)

		try:
			post_object = Post.objects.get(post_id=post_id)
		except:
			return Response({"detail" : "Post does not exist"}, status=status.HTTP_400_BAD_REQUEST)

		self.check_object_permissions(request, post_object)

		try:
			serializer = PostSerializer(post_object)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except:
			return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request):

		username = request.data.get('username')
		post_id  = request.data.get('post_id')
		try:
			user_object = User.objects.get(username=username)
		except:
			return Response({"detail" : "User does not exists"}, status=status.HTTP_400_BAD_REQUEST)

		try:
			post_object = Post.objects.get(post_id=post_id)
		except:
			return Response({"detail" : "Post does not exist"}, status=status.HTTP_400_BAD_REQUEST)

		self.check_object_permissions(request, post_object)

		serializer = PostSerializer(post_object, data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def delete(self, request):
		username = request.data.get('username')
		post_id = request.data.get('post_id')

		try:
			user_object = User.objects.get(username=username)
		except:
			return Response({"detail" : "User does not exists"}, status=status.HTTP_400_BAD_REQUEST)

		try:
			post_object = Post.objects.get(post_id=post_id)
		except:
			return Response({"detail" : "Post does not exist"}, status=status.HTTP_400_BAD_REQUEST)

		self.check_object_permissions(request, post_object)

		try:
			post_object.delete()
			return Response({"detail" : "post deleted"}, status=status.HTTP_200_OK)

		except:
			return Response({"detail" : "Could not delete"}, status=status.HTTP_400_BAD_REQUEST)		