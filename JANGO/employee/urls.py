from django.urls import path
from . import views


urlpatterns =[
    path('',views.empDetails, name='empdetails'),
    path('input',views.dateils),
]