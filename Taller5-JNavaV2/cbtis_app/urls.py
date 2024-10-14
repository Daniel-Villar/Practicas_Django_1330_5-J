from django.urls import path
from cbtis_app import views
urlpatterns = [
    path("", views.ver_lista, name="ver_lista"),
]