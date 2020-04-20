from django.urls import path
from .views import Home, About, Credit_Home


urlpatterns = [
    path('', Home, name='home-page'),
    path('About/', About, name='about-page'),
    path('credithome/', Credit_Home, name='credithome-page')
]
