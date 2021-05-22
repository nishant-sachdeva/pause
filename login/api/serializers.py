from rest_framework import serializers

from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'email', 'password']

		extra_kwargs = {
			'password' : {
				'write_only': True,
			}
		}


	def save(self):
		password = self.validated_data['password']

		email = self.validated_data['email']
		username = self.validated_data['username']

		if User.objects.filter(email=email).exists():
			raise serializers.ValidationError({'error' : 'email already exists'})


		account = User(email=email, username=username)
		account.set_password(password)
		account.save()

		return account