# website urls.py
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('predict',views.predict,name='predict'),
    path('map',views.map,name='map'),
    path('EV Charging',views.EV_Charging,name='EV Charging'),
    path('conclusion',views.conclusion,name='conclusion'),
]
