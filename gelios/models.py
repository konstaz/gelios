from django.db import models


class Users(models.Model):
    user_id = models.PositiveIntegerField()
    creator = models.CharField(max_length=128)  # char
    is_admin = models.BooleanField()  # boolean field
    time_zone = models.CharField(max_length=64)  #  char
    cost_mode = models.CharField(max_length=128)
    legal_name = models.CharField(max_length=128)
    lat_lon = models.FloatField()   # float


class Units(models.Model):
    unit_id = models.PositiveIntegerField()
    creator = models.CharField(max_length=128)  # char
    is_free = models.BooleanField()  # bool
    type = models.CharField(max_length=128)
    unit_icon = models.URLField()   # URL field
    info = models.TextField()   # text field
    created_at = models.DateTimeField(auto_now_add=True)  # datetime
