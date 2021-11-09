from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea, TextInput, ChoiceField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    models = User
    search_fields = ('email', 'last_name', 'first_name', 'phone_number')
    list_filter = ('email', 'last_name', 'first_name',
                   'phone_number', 'is_active', 'is_staff')
    ordering = ('-first_name',)
    list_display = ('email', 'id', 'last_name', 'first_name', 'phone_number',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'last_name', 'first_name', 'phone_number',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'last_name', 'first_name',  'phone_number', 'password1', 'password2', 'is_active', 'is_staff')
        }),
    )


admin.site.register(User, UserAdminConfig)
