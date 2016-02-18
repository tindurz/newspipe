import random
import hashlib
from werkzeug import generate_password_hash
from .abstract import AbstractController
from web.models import User


class UserController(AbstractController):
    _db_cls = User
    _user_id_key = 'id'

    def _handle_password(self, attrs):
        if attrs.get('password'):
            attrs['pwdhash'] = generate_password_hash(attrs.pop('password'))
        elif 'password' in attrs:
            del attrs['password']

    def create(self, **attrs):
        self._handle_password(attrs)
        return super().create(**attrs)

    def update(self, filters, attrs):
        self._handle_password(attrs)
        return super().update(filters, attrs)
