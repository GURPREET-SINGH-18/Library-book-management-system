from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class addstudent(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    enrollment = models.CharField(max_length=15)
    branch = models.CharField(max_length=30)
    year=models.IntegerField()
    sem=models.IntegerField()
    mobile = models.CharField(max_length=13)
    address = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class addbook(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    des=models.TextField(max_length=1200)
    genres=models.CharField(max_length=30)
    year=models.IntegerField()
    student = models.ForeignKey(addstudent,blank=True,null=True,default=None,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='pics')
    language=models.CharField(max_length=20)
    def __str__(self):
        return self.name

