from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('buy',views.buy, name='buy'),
    path('return_ticket', views.return_ticket, name='return_ticket'),
    path('contacts', views.contacts, name='contacts')
]
