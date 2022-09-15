from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from wishlist.models import BarangWishlist

# Create your views here.
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Trisno Bayu Pamungkas'
    }
    return render(request, "wishlist.html", context)

def xml_show_wishlist(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def json_show_wishlist(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def choose_show_wishlist(request, id):
    data = BarangWishlist.objects.filter(pk=id)
    
    if id == 1:
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    elif id == 2:
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
