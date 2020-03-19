from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import candidate, employer


# Create your views here.

def homepage(request):
    return render(request, "login.html")


def login(request):
    if request.method=="POST":
        user = auth.authenticate(username = request.POST['uname'],password=request.POST["pass"])
        if user is not None:
            auth.login(request, user)
            # print(request.user.is_candidate)
            model = candidate.objects.filter(user=request.user)
            try:
                if model[0].is_candidate == True:
                    return redirect("post_candidate")
            except:
                return redirect("post_employer")
        else:
            return render(request, "login.html",{"error":"Invalid login credentials"})
    else:
        return render(request,"login.html")

def signup(request):
    if request.method=="POST":
        if request.POST["pass"]==request.POST["passwordagain"]:
            try:
                user = User.objects.get(username=request.POST["uname"])
                return render(request, "register.html",{"error":"Username has already been taken"})
            except User.DoesNotExist:

                phone_num = request.POST['phone']
                first_name = request.POST["first_name"]
                last_name = request.POST["last_name"]
                email = request.POST["email"]
                user = User.objects.create_user(username=request.POST["uname"], password=request.POST["pass"])
                newcandidate = candidate(phone_num=phone_num, first_name=first_name, user=user, last_name=last_name,
                                         email=email)
                newcandidate.save()
                auth.login(request,user)
                return redirect("login")
        else:
            return render(request,"register.html",{"error":"Password does not match"})
    else:
        return render(request,"register.html")

def signup_emp(request):
    if request.method=="POST":
        if request.POST["pass"]==request.POST["passwordagain"]:
            try:
                user  = User.objects.get(username=request.POST["uname"])
                return render(request, "register_emp.html",{"error":"Username has already been taken"})
            except User.DoesNotExist:
                # phone_num = request.POST['phone']
                phone_num = request.POST['phone']
                first_name = request.POST["first_name"]
                last_name = request.POST["last_name"]
                company_name = request.POST["company_name"]
                email = request.POST["email"]
                user = User.objects.create_user(username=request.POST["uname"], password=request.POST["pass"])
                newemp = employer(first_name=first_name, user=user, last_name=last_name, company_name=company_name,
                                  phone_num=phone_num, email=email)
                newemp.save()
                auth.login(request,user)
                return redirect("login")
        else:
            return render(request,"register_emp.html",{"error":"Password does not match"})
    else:
        return render(request,"register_emp.html")

