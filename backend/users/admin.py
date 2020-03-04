from django.contrib import admin
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import UserProfile


class CustomUserAdmin(UserAdmin):
    model = UserProfile
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        # (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(UserProfile, CustomUserAdmin)

