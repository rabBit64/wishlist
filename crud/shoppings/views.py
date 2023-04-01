from django.shortcuts import render, redirect, get_object_or_404
from .models import WishList
def index(request):
    wishlists = WishList.objects.all()
    context = {
        'wishlists': wishlists,
    }
    return render(request,'shoppings/index.html',context)