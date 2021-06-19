from django.db import models
class Anonce(models.Model):
    teacher=models.CharField(max_length=200,blank=True)
    content=models.TextField(default='no homework ... ',max_length=300)
    avatar=models.ImageField(default='avatar.png',upload_to='avatars/')
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    level= models.CharField(max_length=200 ,default="Pas Important.")
    
    def __str__(self):
        return f"{self.teacher}-{self.created}"