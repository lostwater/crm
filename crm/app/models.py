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
    start_date = models.DateField()
    expect_done_date = models.DateField()
    done_date = models.DateField()
    developers = models.ManyToManyField(Developer)

class Comment(models.Model):
    content =  models.CharField(max_length=50)
    developer = models.ForeignKey(Developer)
    case = models.ForeignKey(Case)
    client = models.ForeignKey(Client)
    date = models.DateField()

class CaseDeveloper(models.Model):
    case = models.ForeignKey(Case)
    developer = models.ForeignKey(Developer)
    role = models.CharField(max_length=50)
    #models.OneToOneField(Case
                         


# Create your models here.
