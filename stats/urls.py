from django.urls import path
from .views import stats, top_bugs, top_features, bug_closure, feature_closure

urlpatterns = [
    path('', stats, name='stats'),
    path('top_bugs', top_bugs),
    path('top_features', top_features),
    path('bug_closure', bug_closure),
    path('feature_closure', feature_closure)
]
