import math
from django.utils import timezone
from tkinter import CASCADE
from django.db import models
from django.forms import FileField

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True,max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=10)
    otp = models.IntegerField(default=456)
    is_verify = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email

class Chairman(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)
    block_no = models.CharField(max_length=10,null=True)
    house_no = models.CharField(max_length=10,null=True)
    pic = models.FileField(upload_to='media/images/',default='media/default_chairman.png')
    about_me = models.TextField(null=True)

    def __str__(self) -> str:
        return self.firstname

class Member(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    dob = models.DateField()
    gender = models.CharField(max_length=15)
    contact = models.CharField(max_length=15)
    email = models.EmailField(unique=True,max_length=30)
    password = models.CharField(max_length=30)
    occupation = models.CharField(max_length=20,null=True)
    block_no = models.CharField(max_length=10,null=True)
    house_no = models.CharField(max_length=10,null=True)
    family_mem = models.IntegerField(null=True)
    total_vehicle = models.IntegerField(null=True)
    pic = models.FileField(upload_to='media/images/',default='media/default_chairman.png')
    about_member = models.TextField(null=True)

    def __str__(self) -> str:
        return self.firstname

class Notice(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    pic = models.FileField(upload_to='media/images/',null=True)
    video = models.FileField(upload_to='media/video/',null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def whenpublished(self):
        timw = timezone.now()
        
        diff= timw - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"

class Notice_View(models.Model):
    notice_id = models.ForeignKey(Notice,on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member,on_delete=models.CASCADE)
    view_at = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    pic = models.FileField(upload_to='media/images/',null=True)
    video = models.FileField(upload_to='media/video/',null=True)
    venue = models.CharField(max_length=50)
    content = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)
    Time = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Event_View(models.Model):
    event_id = models.ForeignKey(Notice,on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member,on_delete=models.CASCADE)
    view_at = models.DateTimeField(auto_now_add=True)
    