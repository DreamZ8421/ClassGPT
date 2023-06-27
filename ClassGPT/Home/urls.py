from django.urls import path
from Home import views

urlpatterns = [
    #path("", views.render_index, name="render_index"),
    #path('menu',views.render_menu,name="render_menu"),
    path("",views.register,name='register'),
    path("menu",views.login,name='login'),
    path("",views.logout,name='logout')
]