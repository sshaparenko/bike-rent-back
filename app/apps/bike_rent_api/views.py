from rest_framework import generics
from apps.bike_rent.models import Bike, BikeCategory, RentOrder, DetailsOrder, DetailCategory, Detail
from .serializers import BikeSerializer, BikeCategorySerializer, RentOrderSerializer, DetailSerializer, DetailCategorySerializer, DetailsOrderSerializer
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser

class BikesList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    parser_classes = [MultiPartParser]

class BikeCategoryList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = BikeCategory.objects.all()
    serializer_class = BikeCategorySerializer

class RentOrderList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = RentOrder.objects.all()
    serializer_class = RentOrderSerializer

class DetailsCategoryList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = DetailCategory.objects.all()
    serializer_class = DetailCategorySerializer

class DetailsList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer

class DetailsOrderList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = DetailsOrder.objects.all()
    serializer_class = DetailsOrderSerializer
