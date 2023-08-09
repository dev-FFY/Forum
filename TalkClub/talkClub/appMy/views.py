from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request,'index.html')

def Register(request):
    return render(request,'register.html')

def Login(request):
    return render(request,'login.html')


def Register(request):

        if request.method=='POST':
                name=request.POST['name']
                email=request.POST['email']
                password=request.POST['password']
                confirm_password=request.POST['confirm_password']
                gender=request.POST['gender']

                if password == confirm_password:
                    if User.objects.filter(username=name).exists():
                        context = {
                            "information": "Bu kullanıcı kullanılıyor, farklı bir kullanıcı adı deneyiniz."
                        }
                        return render(request, 'register.html', context)

                    if User.objects.filter(email=email).exists():

                        context = {
                            "information": "E-mail adresi kullanılıyor farklı bir mail ile kayıt işlemine devam edebilirsiniz."
                            
                        }
                        return render (request,'register.html',context)
                    
                    else:
                        user=User.objects.create_user(username=name,email=email, password=password)
                        user.save()
                        
                        return redirect("kaydol")

                else:
                    context = {
                        "information": "Parolanız girmiş olduğunuz parolayla uyuşmuyor, kontrol ediniz."
                    }

                    return render(request, 'register.html', context)

        return render(request, 'register.html')