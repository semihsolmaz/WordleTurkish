from django.urls import path
from WordleGame import views

app_name = 'WordleGame'

urlpatterns = [
    path('', views.homePage, name='homePage'),
]
