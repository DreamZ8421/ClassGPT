from django.urls import path
from Home import views

urlpatterns = [
    path("", views.render_index, name="render_index")
]