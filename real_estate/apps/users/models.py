from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(uuid.uuid4, editable=False)
    username = models.CharField(verbose_name=_("Username"), max_length=255, unique=True)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=56)
    last_name = models.CharField(verbose_name =_("Last Name"), max_length=56)
    email = models.EmailField(verbose_name = _("Email Address"))
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self) -> str:
        return self.username

    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"
    
    def get_short_name(self):
        return self.first_name