from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MainMain, name='main_main'),
    path('admin/', admin.site.urls),
    path('js/', include('javascript.urls')),
]
