from django.shortcuts import render,redirect
import sys
from datetime import  datetime
from django.apps import apps
from django.http import HttpResponse
from django.contrib.auth.decorators import  login_required
sys.path.append("..")
from userauth.models import candidate,employer,job_posted,applied_for
# Create your views here.
from django.views.generic import ListView,CreateView

@login_required(login_url="/login/")
def home(request):
    data = apps.get_model('userauth.employer').objects.filter(user=request.user)
    print("this is the data",data,request.user)
    return render(request, "showdata.html",{'data':data})

class PostCreateView(CreateView):

    fields = ['job_title','applied_by','posted_on','type','description']
    template_name="jobpost_form.html"

    def form_valid(self, form):
        model = apps.get_model('userauth.job_posted').objects.filter(user=self.request.user)
        form.instance.employer = self.request.user
        return super().form_valid(form)

@login_required(login_url="/login/")
def postcreate(request):
    if request.method=="GET":
        model = employer.objects.filter(user=request.user)
        print(employer.objects.filter(user=request.user))
        # print(model[0].is_candidate)
        if not model:
            print("the user is no employer")
            return redirect("/login/")

        else:
            print("the user is employer",request.user)
            if model[0].is_candidate == False:
                return render(request, "jobpost_form.html")
            else:
                return HttpResponse("this is wrong")

    else:
        job_title = request.POST["job_title"]
        apply_by= request.POST["apply_by"]
        posted_on= request.POST["posted_on"]
        type = request.POST["type"]
        description= request.POST["description"]
        print(job_title,apply_by,posted_on,type,description)
        employer_instance = employer.objects.filter(user=request.user)[0]
        newjob = job_posted.objects.create(employer=employer_instance, job_title=job_title,apply_by=apply_by,posted_on=type,type=type,description=description)
        print("USER LOGGEDIN",request.user)
        model = employer.objects.filter(user=request.user)
        print(employer.objects.filter(user=request.user))
        if not model:
            print("the user is no employer")
            return redirect("/login/")

        else:
            print("the user is employer")
            if model[0].is_candidate==False:
                return redirect("/post_employer")
            else:
                return HttpResponse("this is wrong")

@login_required(login_url="/login/")
def post_employer(request):

    model = employer.objects.filter(user=request.user)
    print("mod",model)
    if not model:
        print("the user is no employer")
        return redirect("/login/")

    else:
        print("the user is employer",request.user.id)
        posts = job_posted.objects.filter(employer=model[0])
        print(posts)
        header="EMPLOYER POSTS"
        if model[0].is_candidate == False:

            return render(request, "jobpost.html",context={"post":posts,"header":header})
            # return HttpResponse(posts)
        else:
            return HttpResponse("this is wrong")

@login_required(login_url="/login/")
def employer_job_applied(request):

    model = employer.objects.filter(user=request.user)
    print("modddddd", model)
    if not model:
        print("the user is no employer")
        return redirect("/login/")

    else:
        print("the user is employer", request.user.id)
        posts = applied_for.objects.filter(job_applied__in=job_posted.objects.filter(employer=model[0]).values_list('id',flat=True))
        print(posts)
        header = "JOBS DASHBOARD"
        if model[0].is_candidate == False:

            return render(request, "appliedjobs.html", context={"post": posts, "header": header})
        else:
            return HttpResponse("this is wrong")


@login_required(login_url="/login/")
def post_candidate(request):

    if request.method=="GET":
        model = candidate.objects.filter(user=request.user)
        print("The user is ", model)
        if not model:
            print("The user is not model")
            return redirect("/login/")
        else:
            print("The user is candidate", request.user.id)
            posts = job_posted.objects.all()
            model_candidate = candidate.objects.filter(user=request.user)[0]
            posts2 = job_posted.objects.exclude(id__in=applied_for.objects.filter(candidate=model_candidate).values_list("job_applied_id",flat=True))
            print(posts,posts2)
            header="CANDIDATE POST"
            # return HttpResponse(posts)
            return render(request, "jobpost.html", context={"post": posts2,"header":header})
    else:
        print(request.POST)
        print(request.POST.get("id"))
        job_applied = job_posted.objects.filter(id=request.POST.get("id"))[0]
        model_candidate = candidate.objects.filter(user = request.user)[0]
        print("jjjjj",job_applied, model_candidate)
        applied_for.objects.create(candidate = model_candidate, job_applied = job_applied, applied_on = datetime.now())
        # return HttpResponse(request.POST)
        return  redirect('post_candidate')

@login_required(login_url="/login/")
def candidate_jobs(request):

    model = candidate.objects.filter(user=request.user)
    print("modddddd", model)
    if not model:
        print("the user is no employer")
        return redirect("/login/")
    else:
        print("the user is candidate", request.user.id, model)
        model_candidate = candidate.objects.filter(user=request.user)[0]
        posts = job_posted.objects.filter(id__in=applied_for.objects.filter(candidate=model_candidate).values_list("job_applied_id", flat=True))
        print(posts)
        header="CANDIDATE APPLIED JOBS"
        # return HttpResponse(posts)
        return render(request, "jobpost.html", context={"post": posts,"header":header})
