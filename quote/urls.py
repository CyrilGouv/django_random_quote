from django.urls import path
from .views import quote_list

app_name = 'quotes'

urlpatterns = [
    path('', quote_list)
]