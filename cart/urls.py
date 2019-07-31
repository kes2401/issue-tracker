from django.urls import path, include
from .views import view_cart, add_to_cart, add_vote_to_cart, update_cart, remove_from_cart
from checkout.views import checkout

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add', add_to_cart, name='add_to_cart'),
    path('add_vote/<id>', add_vote_to_cart, name='add_vote_to_cart'),
    path('update', update_cart, name='update_cart'),
    path('remove/<id>', remove_from_cart, name='remove_from_cart'),
    path('checkout/', include('checkout.urls'))
]