from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as lt
# Create your views here.

def login_view(request):
    return render(request, 'login.html')

def Index(request):
    return render(request,'index.html')

def Register(request):
    return render(request,'register.html')

def Login(request):
    return render(request,'login.html')

def Question(request):
    return render(request,'question.html')

def Post(request):
    return render(request,'post.html')
def Comment(request):
    return render(request,'comment.html')

def Register(request):
    
    if request.method=='POST':
        nickname=request.POST['nickname']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=nickname).exists():
                context={
                    "information":"This nickname is already in use!"
                }
                return render(request,'register.html', context)
            
            if User.objects.filter(email=email).exists():
                
                context = {
                    "information":"This email is already in use!"                    
                }
                return render (request,'register.html',context)
            
            else:
                user=User.objects.create_user(username=nickname, email=email, password=password,)
                user.save()
                
                return redirect("login")
                
        else:
            context={
                "information":"Passwords don't match!"
            }
                
            return render (request,'register.html',context)
                    
    return render(request,'register.html')

def Login(request):
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('main')
        
        else:
            
            context={
                
                "information":"Incorrect"
                
            }
            
            return render(request,'login.html', context)
    
    return render(request,'login.html')

@login_required
def logout(request):
    lt(request)
    return redirect('login')