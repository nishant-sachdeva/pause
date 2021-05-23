from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path

from posts.api.views import PostListAV, PostDetailAV, CreatPostAV


urlpatterns = [
	path('list/', PostListAV.as_view(), name='post_list'),
	path('create/', CreatPostAV.as_view(), name='make_post'),
	path('detail/', PostDetailAV.as_view(), name='post_detail'),
]