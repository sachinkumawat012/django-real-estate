from django.contrib import admin
from .models import Profile
# Register your models here.

admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'gender', 'phone_number', 'country', 'city']
    list_filter = ['gender', 'country', 'city']
    list_display_links = ['id', 'user', 'phone_number']

admin.site.register(Profile, ProfileAdmin)