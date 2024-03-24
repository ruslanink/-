from django.shortcuts import render
from django.http import HttpResponse
from .models import post
import time

# Create your views here.
def home(request):
    posts = post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'index.html', context)


def aboutme(request):
    return render(request, 'aboutme.html')