from django.db import models

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=30)
    password = models.CharField(max_length=30,null=True)

    def __str__(self) -> str:
        return self.firstname
