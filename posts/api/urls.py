from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path

from posts.api.views import PostListAV


urlpatterns = [
	path('posts/', PostListAV.as_view(), name='posts'),
]