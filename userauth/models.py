from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class candidate(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_num = models.CharField(max_length=15)
    is_candidate = models.BooleanField(default=True)

class employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=15)
    is_candidate = models.BooleanField(default=False)


class job_posted(models.Model):
    employer = models.ForeignKey(employer,on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now=True)
    apply_by = models.DateTimeField()
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=200)


class applied_for(models.Model):
    candidate = models.ForeignKey(candidate, on_delete=models.CASCADE)
    job_applied = models.ForeignKey(job_posted, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now=True)
