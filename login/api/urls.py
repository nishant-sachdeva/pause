from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path

from login.api.views import registration_request, logout_view


urlpatterns = [
	path('login/', obtain_auth_token, name='login'),
	path('register/', registration_request.as_view(), name='register'),
	path('logout/', logout_view.as_view(), name='logout_view'),
]