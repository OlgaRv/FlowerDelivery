from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Домашняя страница
    path('users/', include('users.urls')),
    path('catalog/', include('catalog.urls')),
    path('orders/', include('orders.urls')),
]

