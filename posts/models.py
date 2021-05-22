from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Post(models.Model):

	created = models.DateTimeField(auto_now_add=True)
	maker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
		