from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'idx'

urlpatterns = (
	path('', views.home, name = 'home'),
)