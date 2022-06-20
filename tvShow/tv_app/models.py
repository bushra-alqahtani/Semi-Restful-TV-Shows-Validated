from django.db import models
from django.forms import CharField

#for validation

class ShowManager(models.Manager):
    def basic_validation(self,postData):
        errors={ }#create empty dictionary

       #check for the length of title 
        if len(postData["title"]) < 2:
            if len(postData["title"]) == 0:
                errors["title"] = "Title Field is Required"
            else: 
                errors["title"]=" title should be more than 2 chars"
       
        if len(postData["network"])<3:
            if len(postData["network"]) == 0:
                errors["network"] = "Network Field is Required"
            else:
                errors['network']=" title should be more than 3 chars"
        if len(postData['desc']) > 0 and len(postData['desc']) < 10:
            errors['desc']=" title should be more than 10 chars"
        
        return errors




# Create your models here.
class Show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    releseDate=models.DateField()
    desc=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    #override the class of validation 
    objects=ShowManager()
