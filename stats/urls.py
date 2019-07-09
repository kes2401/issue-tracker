from django.urls import path
from .views import stats, top_bugs, top_features

urlpatterns = [
    path('', stats, name='stats'),
    path('top_bugs', top_bugs),
    path('top_features', top_features)
]
