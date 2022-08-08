from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Привет мир!')

def group_posts(request, slug):
    return HttpResponse('Здесь должны быть группы')