from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedUUIDModle

# Create your models here.

User = get_user_model()

class Gender(models.TextChoices):
    MALE="Male", _("Male")
    FEMALE="Female", _("Female")
    OTHER="Other", _("Other")


class Profile(models.Model):
    user = models.OneToOneField(
            User,related_name="profile",
            on_delete=models.CASCADE
        )
    phone_number = PhoneNumberField(
                    verbose_name=_("Phone Number"),
                    max_length = 30, default="+917223962066"
                )
    about_me = models.TextField(
                verbose_name=_("About Me"),
                default="Say somthign about your self"
            )
    license = models.CharField(
                verbose_name=_("Real State License"),
                max_length=20,
                null=True,
                blank=True,
            )
    profile_photo = models.ImageField(
                    verbose_name=_("Profile Photot"),
                    default="/Downloads/c5.png"
            )
    gender = models.CharField(verbose_name=_("Gender"),
                            choices=Gender.choices,
                            default=Gender.OTHER,
                            max_length=20
                        )
    country = CountryField(verbose_name=_("Country"),
                           default="IND",
                           blank=False,
                           null=False,
                        )
    city = models.CharField(verbose_name=_("City"),
                           default="Indore",
                           max_length=200,
                           blank=False,
                           null=False,
                        )
    is_buyer = models.BooleanField(verbose_name=_("Buyer"),
                                   default=False,
                                   help_text="Are you looking to buy a Property?"
                                   )
    is_seller = models.BooleanField(verbose_name=_("Seller"),
                                   default=False,
                                   help_text="Are you looking to sell a Property?"
                                   )
    is_agent = models.BooleanField(verbose_name=_("Agent"),
                                   default=False,
                                   help_text="Are you an Agent?"
                                   )
    top_agent = models.BooleanField(verbose_name=_("Top agent"),
                                   default=False,
                                   )
    rating = models.DecimalField(max_digits=4,
                                 decimal_places=2,
                                 null=True,
                                 blank=True
                                 )
    num_review = models.IntegerField(verbose_name=_("Number of reviews"),
                                     default=0,
                                     null=True,
                                     blank=True,
                                     )
    
    def __str__(self) -> str:
        return f"{self.user.username}'s profile"