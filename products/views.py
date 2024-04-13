from django.shortcuts import render


def index(request):
    return render(request, 'products/index.html', {'title': 'Hello, Django!'})


def products(request):
    return render(request, 'products/products.html', {'title': 'Hello, Django!'})
