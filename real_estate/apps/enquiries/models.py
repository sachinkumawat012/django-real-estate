from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampedUUIDModle

# Create your models here.

class Enquiry(TimeStampedUUIDModle):
    name = models.CharField(
        verbose_name=_("Your name"),
        max_length=100
        )
    phone_number = PhoneNumberField(
        _("Phone number"),
        max_length = 38,
        default = "+910987654321"
    )
    email = models.EmailField(_("Email"))
    subject = models.CharField(_("Subject"), max_length=100)
    message = models.TextField(_("Message"))

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = "Enquiry"
        verbose_name_plural = "Enquirys"