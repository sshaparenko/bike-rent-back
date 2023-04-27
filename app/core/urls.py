from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.bike_rent.urls', namespace='bike_rent')),
    path('api/', include('apps.bike_rent_api.urls', namespace='bike_rent_api')),
]
