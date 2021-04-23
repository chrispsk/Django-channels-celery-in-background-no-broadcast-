from django.urls import path, include
from .views import index, index2

urlpatterns = [
    path('', index, name="home"),
    path('alt/', index2, name="home2"),
]
