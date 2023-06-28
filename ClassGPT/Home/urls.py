from django.urls import path
from . import views

urlpatterns = [
    #path("", views.render_index, name="render_index"),
    path('',views.render_menu,name="render_menu"), #chatbot
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]