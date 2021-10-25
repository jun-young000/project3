from django.urls import path
from chucheon import views

urlpatterns = [
	path('', views.main)
]