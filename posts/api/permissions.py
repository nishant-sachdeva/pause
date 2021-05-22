from rest_framework import permissions


class PostWriterOrAdminOrReadOnly(permissions.BasePermission):
	def has_permission(self,request, view):
		permission = bool((request.user.username == request.data.get('username')) or request.user.is_staff)
		return permission
		# poster himeself or admin : applies to all permissions

	def has_object_permission(self, request, view, object):
		return bool((object.username == request.user) or (request.user.is_staff))
