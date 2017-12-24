from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User


class MultipleAuthBackend(ModelBackend):

    auth_uer_model = User

    def authenticate(self, request, username=None, password=None):
        try:
            user = self.auth_uer_model.objects.get(email=username)
            if check_password(password, user.password):
                return user
            else:
                return None
        except self.auth_uer_model.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return self.auth_uer_model.objects.get(pk=user_id)
        except self.auth_uer_model.DoesNotExist:
            return None
