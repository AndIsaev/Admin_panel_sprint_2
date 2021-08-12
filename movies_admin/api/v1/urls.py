from django.urls import path
from ..v1 import views

urlpatterns = [
    path('movies/', views.MoviesListApi.as_view())
]