from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_dynamic_link, name="create_dynamic_link"),
    path("<str:dynamic_path>/", views.resolve_dynamic_link,
         name="resolve_dynamic_link"),
]
