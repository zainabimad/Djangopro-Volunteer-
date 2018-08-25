from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Uploaded(models.Model):
    title=models.CharField(max_length=200,null=False)
    info=models.CharField(max_length=400,blank=True)
    img=models.FileField(upload_to='docs/')
    up_date=models.DateField(auto_now_add=True)
    uploader=models.CharField(max_length=200,null=False)
    def __str__(self):
        return self.info



