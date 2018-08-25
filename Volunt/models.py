from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.city_name
class Study(models.Model)  :
    certificate = models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.certificate
class Volunteers(models.Model):
    name = models.CharField(max_length=200,null=False)
    age=models.IntegerField()
    birthdate=models.DateField()
    email=models.EmailField(null=False)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    study=models.ForeignKey(Study,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Authentication (models.Model):
    types=[
        ('manger','manger'),
        ('student', 'student'),
        ('teacher', 'teacher'),


    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    user_type=models.CharField(max_length=200,choices=types)
    def __str__(self):
        return self.user.username
