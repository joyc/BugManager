from django.shortcuts import render


def index(request):
    """top page"""
    return render(request, 'home.html')
