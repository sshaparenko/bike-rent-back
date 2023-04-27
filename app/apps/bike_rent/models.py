from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class BikeCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bike_category'

class Bike(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='bike/', null=True)
    description = models.TextField()
    price = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    category = models.ForeignKey(
        BikeCategory, on_delete=models.SET_NULL, default=1, null=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'bike'
    
class RentOrder(models.Model):
    creation_date = models.DateTimeField(default=timezone.now)
    delivery_date = models.DateField(null=True)
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='rent_order'
    )
    bike = models.ManyToManyField(Bike)

    def __str__(self):
        return self.creation_date

    class Meta:
        db_table = 'rent_order'

class DetailCategory(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'detail_category'

class Detail(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='detail/', null=True)
    description = models.TextField()
    price = models.IntegerField(default=0)
    category = models.ForeignKey(
        DetailCategory, on_delete=models.SET_NULL, default=1, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'detail'

class DetailsOrder(models.Model):
    creation_date = models.DateTimeField(default=timezone.now)
    delivery_date = models.DateTimeField(null=True)
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='details_order'
    )
    detail = models.ManyToManyField(Detail)

    def __str__(self):
        return self.creation_date
    
    class Meta:
        db_table = 'details_order'

