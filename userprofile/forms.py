from django import forms
from django.contrib.gis import forms as forms_gis

from django.contrib.auth.models import User
from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email')

class ProfileForm(forms_gis.ModelForm):
    class Meta:
        model = Profile
        fields = ('geom', 'phone')

    location = forms_gis.PointField(widget=
        forms_gis.OSMWidget(attrs={'map_width': 800, 'map_height': 500})
    )