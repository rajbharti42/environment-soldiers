from django.shortcuts import render, redirect
from blog.models import blog, Contact
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def contact(request):
    if request.method =="POST":
        name = request.POST['name']
        address = request.POST['address'] 
        email = request.POST['email']  
        msg = request.POST['textbox']
        contact = Contact(name=name, address=address, email=email, message=msg) 
        contact.save() 

    return render(request, "contact.html")

def ourmotive(request ):
    return render(request, "ourmotive.html")

def blogpost(request, slug):
    blogs = blog.objects.get( slug=slug )
    context = {'blogs':blogs}
    print(context)
    return render(request, "blogpost.html",context)

def blogs(request):
    blogs = blog.objects.all()
    context = {'blogs':blogs}
    # context ={'content': "this is context text"}
    return render(request,"blogs.html", context)