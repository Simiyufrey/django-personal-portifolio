from django.db import models

# Create your models here.


class Service(models.Model):
    s_title=models.CharField(max_length=50)
    s_url=models.ImageField(max_length=30,upload_to="uploads/images")
    s_desc=models.TextField(max_length=200)
    
    
    def __str__(self):
        return self.s_title
    
class Skill(models.Model):
    s_title=models.CharField(max_length=50,unique=True)
    s_url=models.ImageField(max_length=30,upload_to="uploads/images")
    s_perce=models.PositiveIntegerField()
    
   
    def __str__(self):
        return self.s_title
class Message(models.Model):
    email=models.EmailField(max_length=30)
    message=models.TextField(max_length=200,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    entry_type=models.CharField(max_length=10,default="subscribe",blank=True,null=True)
    