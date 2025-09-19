from django.urls import path
from .views import login_view, logout_view, register_view, home

urlpatterns = [
    path('login/',    login_view,    name='login'),
    path('logout/',   logout_view,   name='logout'),
    path('registro/', register_view, name='registro'),
    path('',          home,          name='home'),
]
