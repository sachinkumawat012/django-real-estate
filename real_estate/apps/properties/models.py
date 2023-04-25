from django.db import models
import random
import string
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from apps.common.models import TimeStampedUUIDModle

# Create your models here.
User = get_user_model()

class PropertyPublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super(PropertyPublishedManager, self)
            .get_queryset()
            .filter(published_status=True)
        )
    
class Property(TimeStampedUUIDModle):
    class AdvertType(models.TextChoices):
        FOR_SALE = "For Sale", _("For Sale")
        FOR_RENT =  "For Rent", _("For Rent")
        AUCTION = "Auction", _("Auction")

    class PropertType(models.TextChoices):
        HOUSE = "House", _("House")
        APARTMENT = "Apartment", _("Apartment")
        OFFICE = "Office", _("Office")
        WAREHOUSE = "Warehouse", _("Warehouse")
        COMMERCIAL = "Commercial", _("Commercial")
        OTHER = "Other", _("Other")

    user = models.ForeignKey(
        User,
        verbose_name=_("Agent Seller or Buyer"),
        related_name="agent_buyer",
        on_delete=models.DO_NOTHING,
    )
    title = models.CharField(
        verbose_name=_("Property title"),
        max_length=255,
    )
    slug = AutoSlugField(
        populate_from="title",
        unique=True,
        always_update=True
    )
    ref_code = models.CharField(
        verbose_name=_("Properti refrens code"),
        max_length=255,
        unique=True,
        blank=True
    )
    description = models.TextField(
        verbose_name=_("Property descriptio"),
        default="Please add your property description"

    )
    country = CountryField(
        verbose_name=_("Country"),
        default="IN",
        blank_label = "(select country)",
    )
    city = models.CharField(
        verbose_name=_("City"),
        max_length=180,
        default="Indore"
    )
    postal_code = models.CharField(
        verbose_name=_("Postel code"),
        max_length=144,
        default=453112,
    )
    street_address = models.CharField(
        verbose_name=_("Street address"),
        max_length=250,
        default="Aedi avenue Indore",
    )
    property_number = models.IntegerField(
        verbose_name=_("Property number"),
        validators=[MinValueValidator],
        default=112
    )
    price = models.DecimalField(
        verbose_name=_("Price"),
        max_digits=8,
        decimal_places=2,
        default=0.0
    )
    tax = models.DecimalField(
        verbose_name=_("Property tax"),
        max_digits=6,
        decimal_places=2,
        default=10,
        help_text="10% property tax charged"
    )
    plot_area = models.DecimalField(
        verbose_name=_("Plot area(m^2)"),
        max_digits=8,
        decimal_places=2,
        default=0.0,
    )
    total_floors = models.IntegerField(
        verbose_name=_("Number of floors"),
        default=0
    )
    bedrooms = models.IntegerField(
        verbose_name=_("Bedrooms"),
        default=1,
    )
    bathrooms = models.DecimalField(
        verbose_name=_("Bathrooms"),
        max_digits=4,
        decimal_places=2,
        default=1.0
    )
    advert_type = models.CharField(
        verbose_name=_("Advert type"),
        max_length=60,
        choices=AdvertType.choices,
        default=AdvertType.FOR_SALE
    )
    property_type = models.CharField(
        verbose_name=_("Property_type"),
        max_length=80,
        choices=PropertType.choices,
        default=PropertType.HOUSE
    )
    cover_photo = models.ImageField(
        verbose_name=_("Main property photo"),
        default="c5.png",
        null=True,
        blank=True
    )
    photo1 = models.ImageField(
        default="c5.png",
        null=True,
        blank=True
    )
    photo2 = models.ImageField(
        default="c5.png",
        null=True,
        blank=True
    )
    photo3 = models.ImageField(
        default="c5.png",
        null=True,
        blank=True
    )
    photo4 = models.ImageField(
        default="c5.png",
        null=True,
        blank=True
    )
    published_status = models.BooleanField(
        verbose_name=_("Published statu"),
        default=False
    )
    views = models.IntegerField(
        verbose_name=_("Total views"),
        default=0
    )

    objects = models.Manager()
    published = PropertyPublishedManager()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def save(self, *args, **kwargs):
        self.title = str.title(self.title)
        self.description = str.description(self.description)
        self.ref_code = "".join(random.choices(string.ascii_uppercase) + string.digits, k=10)
        super(Property, self).save(*args, **kwargs)

    @property
    def final_property_price(self):
        tax_percentage = self.tax
        property_price = self.price
        tax_amount = round(tax_percentage * property_price, 2)
        price_with_tax = float(round(tax_amount + property_price, 2))
        return price_with_tax
    

class PropertyViews(TimeStampedUUIDModle):
    ip = models.CharField(
        verbose_name=_("Ip address"),
        max_length=250,
    )
    property = models.ForeignKey(Property, related_name='property_views', on_delete=models.CASCADE),

    def __str__(self) -> str:
        return f"Total views on - {self.property.title} - is {self.property.views} view(s)"
    
    class Meta:
        verbose_name = "Total Views on Property"
        verbose_name_plural = "Total Property views"