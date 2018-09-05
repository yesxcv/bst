from django.http import HttpResponse
from django.urls import path
from . import views
from django.views.generic.base import RedirectView
urlpatterns = [
	path('',views.index,name='index'),
]