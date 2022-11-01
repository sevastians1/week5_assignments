from django.urls import path
from . import views
urlpatterns = [
    path("", views.main_page),
    path("get_pokemon/<str:name>/", views.get_pokemon),
]