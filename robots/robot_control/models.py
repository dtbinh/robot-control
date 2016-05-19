from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.db import models

# Create your models here.

class Robot(models.Model):
    name = models.CharField(max_length=200)

class Session(models.Model):
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(auto_now=True)
    num_votes = models.IntegerField()

class Votes(models.Model):
    UP = 'U'
    DOWN = 'D'
    LEFT = 'L'
    RIGHT = 'R'
    VOTE_CHOICES = (
        (UP, 'up'),
        (DOWN, 'down'),
        (LEFT, 'left'),
        (RIGHT,'right'),
    )
    robot = models.ForeignKey(Robot)
    vote_date = models.DateTimeField(auto_now=True)
    session = models.ForeignKey(Session, db_index=True)
    vote = models.CharField(max_length=1, choices=VOTE_CHOICES)
    username = models.ForeignKey(settings.AUTH_USER_MODEL)

class CustomUserManager(BaseUserManager):
    def create_user(self, username, control_robot=None, password=None):
        user = self.model(username=username, control_robot=control_robot)
        return user

    def create_superuser(self,username, password):
        user = self.create_user(username=username, password=password)
        user.is_staff = True
        user.is_superuser=True
        user.save()
        return user



class CustomUser(AbstractBaseUser, PermissionsMixin):
    '''
    custom user class
    '''
    username = models.CharField(max_length=200, unique=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    control_robot = models.ForeignKey(Robot, null=True)
    email = models.CharField(max_length=200,null=True)
    first_name= models.CharField(max_length=200,null=True)
    last_name = models.CharField(max_length=200,null=True)

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    def __unicode__(self):
        return self.username
