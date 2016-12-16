from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^buy/$', views.buyStocks, name='index'),
]