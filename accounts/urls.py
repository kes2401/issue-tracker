from django.urls import path, include
from .views import login, logout, register, profile
from accounts import url_reset

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('password_reset/', include(url_reset)),
    path('profile/', profile, name='profile')
]
