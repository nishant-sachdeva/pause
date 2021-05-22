from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Post(models.Model):
	post_id = models.AutoField(primary_key=True)
	created = models.DateTimeField(auto_now_add=True)
	username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
	content = models.TextField(blank=True)

