from django.urls import path
from .views import tracker, create_bug, create_feature, feature_detail, bug_detail, add_comment

urlpatterns = [
    path('tracker/', tracker, name='tracker'),
    path('tracker/create_bug', create_bug, name='create_bug'),
    path('tracker/create_feature', create_feature, name='create_feature'),
    path('tracker/bug_detail/<id>/', bug_detail, name='bug_detail'),
    path('tracker/feature_detail/<id>/', feature_detail, name='feature_detail'),
    path('tracker/issue_detail/<id>/add_comment', add_comment),
]
