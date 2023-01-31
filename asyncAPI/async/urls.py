from django.urls import path
from . import views


urlpatterns = [
    path('async', views.AsyncViewSet.as_view(), name='async-call'),
]