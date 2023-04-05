from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):

    def email_validate(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Please provide valid email address"))
        
    def create_user(self, username, first_name, last_name, email, password, **extra_fields):
        
        if not username:
            raise ValueError(_("Please provide username"))
        
        if not first_name:
            raise ValueError(_("Please provide first_name"))
        
        if not last_name:
            raise ValueError(_("Please provide last_name"))

        if email:
            email = self.normalize_email(email)
            self.email_validate(email)
        else:
            raise ValueError(_("An email address is required"))
        
        user = self.model(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email
            **extra_fields
        )
        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password, first_name, last_name, email, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get["is_staff"] != True:
            raise ValueError(_("Superuser must have is_staff=True"))
        
        if extra_fields.get["is_superuser"] != True:
            raise ValueError(_("Superuser must have is_superuser=True"))
        
        if not password:
            raise ValueError("Password is required")
        
        if email:
            email = self.normalize_email(email)
            self.email_validate(email)
        else:
            raise ValidationError("Admin Account: An email address is required for the superuser")
        user = self.create_user(username, first_name, last_name, email, password, **extra_fields)
        user.save(using=self._db)
        return user
    