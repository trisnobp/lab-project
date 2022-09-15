from xml.etree.ElementInclude import include
from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import xml_show_wishlist
from wishlist.views import json_show_wishlist
from wishlist.views import choose_show_wishlist

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', xml_show_wishlist, name='xml_show_wishlist'),
    path('json/', json_show_wishlist, name='json_show_wishlist'),
    path('json/<int:id>', choose_show_wishlist, name='choose_show_wishlist')

]

