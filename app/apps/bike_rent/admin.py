from django.contrib import admin
from . import models

admin.site.register(models.Bike)
admin.site.register(models.BikeCategory)
admin.site.register(models.RentOrder)
