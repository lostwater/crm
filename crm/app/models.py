from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    name = models.CharField(max_length=50)

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roles = models.ManyToManyField(Role)

class Case(models.Model):
    CASE_STATUS = (
        (1, 'Pre'),
        (2, 'Ing'),
        (3, 'Past'),
    )
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Client)
    status = models.IntegerField(choices=CASE_STATUS)
    startdate = models.DateField(blank=True, null=True)
    expect_donedate = models.DateField(blank=True, null=True)
    donedate = models.DateField(blank=True, null=True)
    developers = models.ManyToManyField(Developer)

class Comment(models.Model):
    content =  models.TextField()
    developer = models.ForeignKey(Developer,null=True)
    case = models.ForeignKey(Case,null=True)
    client = models.ForeignKey(Client,null=True)
    date = models.DateField(blank=True, null=True)

class CaseDeveloper(models.Model):
    case = models.ForeignKey(Case)
    developer = models.ForeignKey(Developer)
    role = models.CharField(max_length=50)
    #models.OneToOneField(Case)

class SysLog(models.Model):
    date = models.DateField()
    operator = models.CharField(max_length=50)
    content =  models.TextField()
    

# Create your models here.
