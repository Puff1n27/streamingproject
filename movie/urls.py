from django.urls import path
from .views import home,movie_detail

app_name = "movie"

urlpatterns = [
    path('', home, name='home'),
    path('movie/<str:movie_type>/<int:pk>/', movie_detail, name='movie_detail'),
]
