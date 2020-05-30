from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=30)
    mail=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    psw=models.CharField(max_length=30)
    pswr=models.CharField(max_length=30)

    def __str__(self):
        return self.name


