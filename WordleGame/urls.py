from django.urls import path
from WordleGame import views

app_name = 'wikodeApp'

urlpatterns = [
    path('', views.homePage, name='homePage'),
]
