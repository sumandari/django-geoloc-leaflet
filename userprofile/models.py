from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as gis_models


class Profile(gis_models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    location = gis_models.PointField()
    address = models.CharField(max_length=100)
