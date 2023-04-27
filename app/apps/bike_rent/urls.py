from django.urls import path
from django.views.generic import TemplateView

app_name = 'bike_rent'

urlpatterns = [
    path('', TemplateView.as_view(template_name="bike_rent/index.html")),
]