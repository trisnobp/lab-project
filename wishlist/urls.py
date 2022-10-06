from xml.etree.ElementInclude import include
from django.urls import path
from wishlist.views import show_wishlist, tambah_wishlist
from wishlist.views import xml_show_wishlist
from wishlist.views import json_show_wishlist
from wishlist.views import choose_show_wishlist
from wishlist.views import register
from wishlist.views import login_user
from wishlist.views import logout_user
from wishlist.views import show_wishlist_ajax
from wishlist.views import tambah_wishlist

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', xml_show_wishlist, name='xml_show_wishlist'),
    path('json/', json_show_wishlist, name='json_show_wishlist'),
    path('json/<int:id>', choose_show_wishlist, name='choose_show_wishlist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('ajax/', show_wishlist_ajax, name = 'show_wishlist_ajax'),
    path('ajax/submit/', tambah_wishlist, name = 'tambah_wishlist'),

]

