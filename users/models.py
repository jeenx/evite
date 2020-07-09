import logging

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

logger = logging.getLogger(__name__)


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def full_name(self):
        return self.get_full_name()

    def get_full_name(self):
        """
        Return first name and last name combined as the full name
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        if not len(full_name.strip()):
            full_name = self.email
        return full_name.strip()

    def __str__(self):
        return self.email
