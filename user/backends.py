from app.models import User
from multipleauth.backends import MultipleAuthBackend


class UserAuthBackend(MultipleAuthBackend):

    auth_uer_model = User
