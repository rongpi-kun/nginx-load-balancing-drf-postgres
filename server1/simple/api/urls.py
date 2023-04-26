from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowBooks.as_view()),
]