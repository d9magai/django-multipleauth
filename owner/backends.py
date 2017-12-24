from app.models import Owner
from multipleauth.backends import MultipleAuthBackend


class OwnerAuthBackend(MultipleAuthBackend):

    auth_uer_model = Owner
