from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from django.contrib.auth.models import User
from .models import Profile


class UserProfileInline(OSMGeoAdmin, admin.StackedInline):
    model = Profile
    fk_name = 'user'

    def __init__(self, parent_model, admin_site):
        self.admin_site = admin_site
        self.parent_model = parent_model
        self.opts = self.model._meta
        self.has_registered_model = admin_site.is_registered(self.model)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    fields = ('username', 'first_name', 'last_name', 'last_login', 'email')
    list_select_related = True
    inlines = [
        UserProfileInline,
    ]

    def get_userprofile_name(self, instance):
        # instance is User instance
        return instance.get_profile().name

admin.site.unregister(User)
admin.site.register(User, UserAdmin)