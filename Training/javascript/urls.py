from django.urls import path, include
from . import views


app_name = 'javascript'
urlpatterns = [
    path('main/', views.MainJS, name='main_js'),

]
