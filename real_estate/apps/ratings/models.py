from django.db import models
from django.utils.translation import gettext_lazy as _
from real_estate.settings.base import AUTH_USER_MODEL
from apps.common.models import TimeStampedUUIDModle
from apps.profiles.models import Profile

# Create your models here.

class Rating(TimeStampedUUIDModle):

    class Range(models.IntegerChoices):
        RATING_1 = 1, _("Poor")
        RATING_2 = 2, _("Fair")
        RATING_3 = 3, _("Good")
        RATING_4 = 4, _("Very Good")
        RATING_5 = 5, _("Excellent")

    rater = models.ForeignKey(
                AUTH_USER_MODEL,
                verbose_name=_("User providing the rating"),
                on_delete=models.SET_NULL,
                null=True,
                )
    agent  = models.ForeignKey(
                Profile,
                verbose_name = _("Agent being rated"), 
                on_delete=models.SET_NULL,
                null=True,
                related_name="agent_review"
                )
    rating = models.IntegerField(
                verbose_name=_("Rating"),
                choices=Range.choices,
                help_text="1=Poor, 2=Fail, 3=Good, 4=Very Good, 5=Excelent",
                default=0,
                )
    commet = models.TextField(verbose_name=_("Comments"))

    class Meta:
        unique_together = ["rater", "agent"]

    def __str__(self) -> str:
        return f"{self.agent} rated at {self.rating}"
