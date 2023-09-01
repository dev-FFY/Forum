from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as lt
from django.shortcuts import render, get_object_or_404
from .models import Author, Category, Post
# Create your views here.



def Index(request):
    return render(request,'index.html')


def Question(request):
    return render(request,'question.html')

def Comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        "post": post
    }
    
    return render(request,'comment.html', context)

def Post(request):
    return render(request,'post.html')




