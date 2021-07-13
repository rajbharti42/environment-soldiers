from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name', 'default')
        last_name = request.POST.get('last_name', 'default')
        username = request.POST.get('username', 'default')
        email = request.POST.get('email', 'default')
        password1 = request.POST.get('password1', 'default')
        password2 = request.POST.get('password2', 'default')
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exists try another username")
                return render(request ,'signup.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return render(request ,'signup.html')
            else:
                user = User.objects.create_user(username=username , email =email, first_name=first_name,  last_name = last_name, password =password1 )
                user.save()
                messages.info(request, 'user successfully created')
                return redirect("blog")
        else:
            messages.info(request,"Your Password Is Not Match Please Conform your Password")
            return render(request ,'signup.html')
    else:
        return render(request ,'signup.html')
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("blog")
        else:
            messages.info(request,"invalid credentials")
            return redirect("login")


    return render(request, 'login.html')
   