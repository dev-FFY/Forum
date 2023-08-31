from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as lt
# Create your views here.



def Index(request):
    return render(request,'index.html')


def Question(request):
    return render(request,'question.html')

def Post(request):
    return render(request,'post.html')

def Comment(request):
    return render(request,'comment.html')



