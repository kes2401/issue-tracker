from django.urls import path
from .views import tracker, create_bug, create_feature

urlpatterns = [
    path('tracker/', tracker, name='tracker'),
    path('tracker/create_bug', create_bug, name='create_bug'),
    path('tracker/create_feature', create_feature, name='create_feature'),
]
