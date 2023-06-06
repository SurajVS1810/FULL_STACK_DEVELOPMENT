from django.urls import path
from . import views

urlpatterns=[
    path('',views.owner,name='owner'),
    path('client',views.client,name='client'),
    path('place',views.place,name='place'),
]