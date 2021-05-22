from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path

from posts.api.views import PostListAV, PostDetailAV


urlpatterns = [
	path('list/', PostListAV.as_view(), name='post_list'),
	path('detail/', PostDetailAV.as_view(), name='post_detail'),
]