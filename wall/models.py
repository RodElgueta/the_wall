from django.db import models
from datetime import datetime
from .validators import UsersManager

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=45,unique=True)
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    email = models.EmailField(max_length=155,unique=True)
    password = models.CharField(max_length=255)
    allowed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    followed = models.ManyToManyField('Users',related_name='followers')
    objects = UsersManager()

    def __str__(self) -> str:
        return f'{self.id} {self.name}'

class Messages(models.Model):
    message = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Users,related_name='messages',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.id} {self.user}'

class Comments(models.Model):
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Users,related_name='comments',on_delete=models.CASCADE)
    message = models.ForeignKey(Messages,related_name='msg_comments',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.id} {self.user} {self.message}'



















