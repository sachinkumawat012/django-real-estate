from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import CustomeUserChangeForm, CustomeUserCreationForm
from .models import User
# Register your models here.


class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    add_form = CustomeUserCreationForm
    form = CustomeUserChangeForm
    model = User
    # used for making the fields/values clickable
    list_display_links = [
        'id',
        'email',
        ]
    list_display = [
        'id',
        'pkid',
        'email',
        'username',
        'first_name',
        'last_name',
        'is_active'
        'is_staff',
        ]
    list_filter = [
        'email',
        'username',
        'first_name',
        'last_name',
        'is_active'
        'is_staff',
        ]
    fieldsets = (
        (
            _("Login Credentials"),
            {"fields":('email', 'password',)},
        ),
        (
            _('Personal Information'),
            {'fields':('username', 'first_name', 'last_name',)},
        ),
        (
            _('Permissions and Groups'),
            {'fields':('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)},
        ),
        (
            _('Importent Dates'),
            {'fields':('last_login', 'date_joined',)},
        ),
    )
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('email', 'password1', 'password2', 'is_staff', 'is_active',),
        })
    )
    search_fields = ['email', 'username', 'first_name', 'last_name']

admin.site.register(User, UserAdmin)