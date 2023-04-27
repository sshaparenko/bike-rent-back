from rest_framework import serializers
from apps.bike_rent.models import Bike, BikeCategory, RentOrder, Detail, DetailCategory, DetailsOrder

class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = ('id', 'name', 'image', 'description', 'price', 'number', 'category')

class BikeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeCategory
        fields = ('id', 'name')

class RentOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentOrder
        fields = ('id', 'creation_date', 'delivery_date', 'client', 'bike')

class DetailCategorySerializer:
    class Meta:
        model = DetailCategory
        fields = ('id', 'name')

class DetailSerializer:
    class Meta:
        model = Detail
        fields = ('id', 'name', 'image', 'description', 'price', 'category')

class DetailsOrderSerializer:
    class Meta:
        model = DetailsOrder
        fields = ('id', 'creation_date', 'delivery_date', 'client', 'detail')