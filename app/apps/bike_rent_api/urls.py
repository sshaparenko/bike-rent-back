from django.urls import path
from .views import BikesList, BikeCategoryList, RentOrderList, DetailsCategoryList, DetailsList, DetailsOrderList
from django.conf import settings
from django.conf.urls.static import static

app_name = 'bike_rent_api'

urlpatterns = [
    path('bikes/', BikesList.as_view(), name='bike'),
    path('bikes/categories/', BikeCategoryList.as_view(), name='bike_category'),
    path('order/bike/', RentOrderList.as_view(), name='rent_order'),
    path('details/', DetailsList.as_view(), name='details'),
    path('details/categories/', DetailsCategoryList.as_view(), name='detail_category'),
    path('order/details/', DetailsOrderList.as_view(), name='details_order'),
] + static(settings.MEDIA_URL.replace('/api', ''), document_root=settings.MEDIA_ROOT)