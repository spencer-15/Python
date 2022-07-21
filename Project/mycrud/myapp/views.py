from multiprocessing import context
from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    if request.POST:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        subject = request.POST['subject']

        sid = Student.objects.create(firstname=firstname,
                                     lastname = lastname,
                                     email = email,
                                     password = password,
                                     subject = subject)
        
        if sid:
            context ={
                "s_msg" : "Successfully data inserted"
            }
            return render(request,"myapp/index.html",context)
        else:
            context ={ 
                "s_msg" : "Successfully data inserted"
            }
            return render(request,"myapp/index.html",context)

    return render(request,"myapp/index.html")    

def dashboard(request):
    sall =Student.objects.all()
    context= {
        "sall" : sall,
    }
    print("----> sall",sall)
    return render(request,"myapp/dashboard.html",context)