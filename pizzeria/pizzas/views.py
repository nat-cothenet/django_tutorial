from django.shortcuts import render

def index(request):
    """The home page for Pizza Topper"""
    return render(request, 'pizzas/index.html')