from django.urls import path
from .views import view_cart, add_to_cart, update_cart, remove_from_cart

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add', add_to_cart, name='add_to_cart'),
    path('update', update_cart, name='update_cart'),
    path('remove/<id>', remove_from_cart, name='remove_from_cart')
]