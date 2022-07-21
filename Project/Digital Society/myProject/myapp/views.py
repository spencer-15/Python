from http.client import HTTPResponse
from tkinter import Button
from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from .models import *

from django.core.mail import send_mail
from random import *

# Create your views here.
def home(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "chairman":
            cid = Chairman.objects.get(user_id = uid)
            context = {
                "uid":uid,
                "cid":cid,
            }
            return render(request,"myapp/index.html",context)
        else:
            uid = User.objects.get(email = request.session['email'])
            mid = Member.objects.get(user_id = uid)
            context = {
                "uid":uid,
                "mid":mid,
            }
            return render(request,"myapp/index-member.html",context)

    else:
        return render(request,"myapp/login.html")

def about(request):
    return HttpResponse("<h1>About page</h1>")

@csrf_exempt
def login(request):
    if "email" in request.session:
        return redirect("home")
    else:
        if request.POST:
            p_email = request.POST['email']
            p_password = request.POST['password']
            try:
                uid = User.objects.get(email = p_email)
                if uid.password == p_password and uid.role=="chairman":
                    cid = Chairman.objects.get(user_id = uid)
                    request.session["email"] = p_email
                    context = {
                        "uid" : uid,
                        "cid" : cid,
                    }
                    
                    return render(request,"myapp/index.html",context)
                elif uid.password == p_password and uid.role=="member":
                    if uid.is_verify:
                        mid = Member.objects.get(user_id = uid)
                        request.session["email"] = p_email
                        context = {
                            "uid" : uid,
                            "mid" : mid,
                        }
                        return render(request,"myapp/index-member.html",context)
                    else:
                        uid = User.objects.get(email = p_email)
                        mid = Member.objects.get(user_id = uid)
                        context = {
                            "uid":uid,
                            "mid":mid,
                        }
                        return render(request,"myapp/change-password.html",context)
                else:
                    context = {
                    "e_msg" : "Invalid password"
                    }
                    return render(request,"myapp/login.html",context)
            except Exception as e:
                print("exception ====================",e)
                context = {
                    "e_msg" : "Invalid email address"
                }
                return render(request,"myapp/login.html",context)
        else:
            print("---> page just loaded")
            return render(request,"myapp/login.html")

def logout(request):
    if "email" in request.session:
        del request.session['email']
        return render(request,"myapp/login.html")
    else:
        return render(request,"myapp/login.html")

def profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "chairman":
            cid = Chairman.objects.get(user_id = uid)
            context = {
                "uid" : uid,
                "cid" : cid,
             }
            return render(request,"myapp/profile.html",context)
        elif uid.role == "member":
            uid = User.objects.get(email = request.session['email'])
            mid = Member.objects.get(user_id = uid)
            context = {
                "uid" : uid,
                "mid" : mid,
             }
            return render(request,"myapp/profile-member.html",context)

def change_password(request):
    if "email" in request.session:
        if request.POST:
            currentpassword = request.POST['currentpassword']
            newpassword = request.POST['newpassword']
            uid = User.objects.get(email = request.session['email'])
            if uid.role=='chairman':
                if uid.password == currentpassword:
                    uid.password = newpassword
                    uid.save()
                    cid = Chairman.objects.get(user_id = uid)
                    context = {
                        'msg' : "Successfully password reset",
                        "uid" : uid,
                        "cid" : cid,
                    }
                    return render(request,"myapp/profile.html",context)
                else:
                    cid = Chairman.objects.get(user_id = uid)
                    context = {
                        "uid" : uid,
                        "cid" : cid,
                        'msg' : "Invalid password"
                    }
                    return render(request,"myapp/profile.html",context)
            elif uid.role=='member':
                if uid.password == currentpassword:
                    uid.password = newpassword
                    uid.save()
                    mid = Member.objects.get(user_id = uid)
                    context = {
                        'msg' : "Successfully password reset",
                        "uid" : uid,
                        "mid" : mid,
                    }
                    return render(request,"myapp/profile-member.html",context)
                else:
                    mid = Member.objects.get(user_id = uid)
                    context = {
                        "uid" : uid,
                        "mid" : mid,
                        'msg' : "Invalid password"
                    }
                    return render(request,"myapp/profile-member.html",context) 
            else:
                pass
        else:
            return redirect("profile")
    else:
        return redirect("login")

def update_profile(request):
    if "email" in request.session:
        if request.POST:
            uid = User.objects.get(email = request.session['email'])
            if uid.role=='chairman':
                cid = Chairman.objects.get(user_id = uid)
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                block_no = request.POST['block_no']
                house_no = request.POST['house_no']
                if "pic" in request.FILES:
                    cid.pic = request.FILES['pic']
                    cid.save()
                about_me = request.POST['about_me']

                cid.firstname = firstname
                cid.lastname = lastname
                cid.block_no = block_no
                cid.house_no = house_no
                cid.about_me = about_me
                cid.save()
                return redirect("profile") 

            elif uid.role=='member':
                uid = User.objects.get(email = request.session['email'])
                mid = Member.objects.get(user_id = uid)
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                dob = request.POST['dob']
                gender = request.POST['gender']
                contact = request.POST['contact']
                occupation = request.POST['occupation']
                block_no = request.POST['block_no']
                house_no = request.POST['house_no']
                family_mem = request.POST['family_mem']
                total_vehicle = request.POST['total_vehicle']
                if "pic" in request.FILES:
                    mid.pic = request.FILES['pic']
                    mid.save()
                about_me = request.POST['about_me']

                mid.firstname = firstname
                mid.lastname = lastname
                mid.dob = dob
                mid.gender = gender
                mid.conatct = contact
                mid.occupation = occupation
                mid.block_no = block_no
                mid.house_no = house_no
                mid.about_me = about_me
                mid.family_mem = family_mem
                mid.total_vehicle = total_vehicle
                mid.save()
                uid = User.objects.get(email = request.session['email'])
                mid = Member.objects.get(user_id = uid)
                context = {
                    "uid" : uid,
                    "mid" : mid,
                }
                return render(request,"myapp/profile-member.html", context)       
            else:
                pass       

        else:
           return redirect("profile") 
    else:
        return redirect("login")

def add_member(request):   
    if 'email' in request.session:
        if request.POST:
            uid = User.objects.get(email = request.session['email'])
            cid = Chairman.objects.get(user_id = uid)
            email = request.POST['email']
            contact = request.POST['contact'],

            data = ["sd4c45","345ccg","45fxc9","df9843c","898ffd","sd7834c"]
            c_no = str(contact[4:9])
            e = str(email[5:8])
            password = choice(data)+c_no+e
            
            u_id = User.objects.create(email = request.POST['email'],
                                        password = password,
                                        role = 'member',
                                        )
            mid = Member.objects.create(
                user_id = u_id,
                firstname = request.POST['firstname'],
                lastname = request.POST['lastname'],
                gender = request.POST['gender'],
                dob = request.POST['dob'],
                contact = request.POST['contact'],
                email = request.POST['email'],
                
                occupation = request.POST['occupation'],
                block_no = request.POST['block_no'],
                house_no = request.POST['house_no'],
                family_mem = request.POST['family_mem'],
                total_vehicle = request.POST['total_vehicle'],
                about_member = request.POST['about_member'],
            )
            if "pic" in request.FILES:
                mid.pic = request.FILES['pic']
                mid.save()
                u_id.save()
            
            context ={
                    "uid" : uid,
                    "cid" : cid,
            }
            mid.save()
            u_id.save()
            msg = "your password is "+str(password)
            send_mail("Password confirmation",msg,"digital.society05@gmail.com",[email])
            return render(request,"myapp/add-member.html",context)
        else:
            uid = User.objects.get(email = request.session['email'])
            cid = Chairman.objects.get(user_id = uid)
            context ={
                    "uid" : uid,
                    "cid" : cid,
            }
            return render(request,"myapp/add-member.html",context)
    else:
        return redirect("login")

def view_member(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])   
        if uid.role == "chairman":
            cid = Chairman.objects.get(user_id=uid)
            mall = Member.objects.all()
            context ={
                "uid" : uid,
                "cid" : cid,
                "mall" : mall,
            }
            return render(request,"myapp/view-member.html",context)
        elif uid.role == "member":
            uid = User.objects.get(email = request.session['email'])
            mid = Member.objects.get(user_id=uid)
            mall = Member.objects.all()
            context ={
                "uid" : uid,
                "mid" : mid,
                "mall" : mall,
            }
            return render(request,"myapp/view-member-member.html",context)
        else:
            uid = User.objects.get(email = request.session['email'])    
            cid = Chairman.objects.get(user_id=uid)
            context ={
                "uid" : uid,
                "cid" : cid,
            }
            return render(request,"myapp/view-member.html",context)
    else:
        return redirect("login")


def add_notice(request):
    if "email" in request.session:
        if request.POST:
            uid = User.objects.get(email = request.session['email'])
            cid = Chairman.objects.get(user_id = uid)

            nid = Notice.objects.create(
                user_id = uid,
                title = request.POST['title'],
                content = request.POST['content'],
            )
            
            if "pic" in request.FILES:
                nid.pic = request.FILES['pic']

            if "video" in request.FILES:
                nid.video = request.FILES['video']

            nid.save()

            if nid:
                context ={
                    's_msg' : 'Successfully Notice Uploaded',
                    "uid" : uid,
                    "cid" : cid,
                }
                return render(request,"myapp/add-notice.html",context)
            else:
                return render(request,"myapp/add-notice.html")
        else:
            uid = User.objects.get(email = request.session['email'])
            cid = Chairman.objects.get(user_id = uid)
            context ={
                "uid" : uid,
                "cid" : cid,
            }
            return render(request,"myapp/add-notice.html",context)
    else:
        return redirect("login")

def view_notice(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "chairman":
            cid = Chairman.objects.get(user_id=uid)
            nall = Notice.objects.all()
            context ={
                "uid" : uid,
                "cid" : cid,
                "nall" : nall,
            }
            return render(request,"myapp/view-notice.html",context)
        elif uid.role == "member":
            uid = User.objects.get(email = request.session['email'])
            mid = Member.objects.get(user_id=uid)
            nall = Notice.objects.all()
            context ={
                "uid" : uid,
                "mid" : mid,
                "nall" : nall,
            }
            return render(request,"myapp/view-notice-member.html",context)
        else:
            uid = User.objects.get(email = request.session['email'])
            cid = Chairman.objects.get(user_id = uid)
            context ={
                "uid" : uid,
                "cid" : cid,
            }
            return render(request,"myapp/view-notice.html",context)   
    else:
        return redirect("login")

def add_event(request):
    if "email" in request.session:
        if request.POST:
            uid = User.objects.get(email = request.session['email'])
            cid = Chairman.objects.get(user_id = uid)

            eid = Event.objects.create(
                user_id = uid,
                title = request.POST['title'],
                content = request.POST['content'],
                venue = request.POST['venue'],
                Date = request.POST['Date'],
                Time = request.POST['Time']
            )
            
            if "pic" in request.FILES:
                eid.pic = request.FILES['pic']

            if "video" in request.FILES:
                eid.video = request.FILES['video']

            eid.save()

            if eid:
                context ={
                    's_msg' : 'Successfully Event Uploaded',
                    "uid" : uid,
                    "cid" : cid,
                }
                return render(request,"myapp/add-event.html",context)
            else:
                return render(request,"myapp/add-event.html")
        else:
            uid = User.objects.get(email = request.session['email'])
            cid = Chairman.objects.get(user_id = uid)
            context ={
                "uid" : uid,
                "cid" : cid,
            }
            return render(request,"myapp/add-event.html",context)
    else:
        return redirect("login")

def view_event(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "chairman":
            cid = Chairman.objects.get(user_id=uid)
            eall = Event.objects.all()
            context ={
                "uid" : uid,
                "cid" : cid,
                "eall" : eall,
            }
            return render(request,"myapp/view-event.html",context)
        elif uid.role == "member":
            uid = User.objects.get(email = request.session['email'])
            mid = Member.objects.get(user_id=uid)
            eall = Event.objects.all()
            context ={
                "uid" : uid,
                "mid" : mid,
                "eall" : eall,
            }
            return render(request,"myapp/view-event-member.html",context)
        else:
            uid = User.objects.get(email = request.session['email'])
            cid = Chairman.objects.get(user_id = uid)
            context ={
                "uid" : uid,
                "cid" : cid,
             }    

    else:
        return redirect("login")
        

def update_password(request):
    email = request.POST['email']
    password = request.POST['password']
    newpassword= request.POST['newpassword']
    repassword= request.POST['repassword']

    uid = User.objects.get(email = email)
    if uid.password == password:
        if newpassword==repassword:
            uid.password = newpassword
            uid.is_verify = True
            uid.is_active = True
            uid.save()
        else:
            pass
    else:
        pass
    return redirect("login")