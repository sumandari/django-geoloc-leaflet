from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from django.contrib.auth.models import User
from .models import Profile


class UserProfileInline(OSMGeoAdmin, admin.StackedInline):
    """
    create class for profile inline view in User Admin page
    Inhereit OSMGeoAdmin to get a good map view
    """
    model = Profile
    fk_name = 'user'

    def __init__(self, parent_model, admin_site):
        self.admin_site = admin_site
        self.parent_model = parent_model
        self.opts = self.model._meta
        self.has_registered_model = admin_site.is_registered(self.model)


class UserAdmin(OSMGeoAdmin, admin.ModelAdmin):
    """
    using inline attribute to show profile model
    """
    list_display = ('username', 'last_login', 'get_phone')
    ordering = ('first_name',)

    fields = ('username', 'first_name', 'last_name', 'last_login', 'email')

    # set True, will call select_related('user', 'profile'),
    # query with fk presented
    list_select_related = True

    inlines = [
        UserProfileInline,
    ]

    # get phone from profile
    def get_phone(self, obj):
        return obj.profile.phone
    # rename colomn list display
    get_phone.short_description = 'phone'

    # override to restrict user view
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(id=request.user.id)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
