from django.db import models

# Create your models here.
class user_profile_details(models.Model):
    user_id=models.IntegerField(default=None)
    gender=models.CharField(max_length=10,blank=True,null=True,default=None)
    mobile_no=models.IntegerField(default=None)
    location=models.CharField(max_length=100,blank=True,null=True,default=None)
    Education=models.CharField(max_length=100,blank=True,null=True,default=None)
    Profession=models.CharField(max_length=100,blank=True,null=True,default=None)
    collage_name=models.CharField(max_length=100,blank=True,null=True,default=None)
    interested_filed=models.CharField(max_length=100,blank=True,null=True,default=None)
    user_bio=models.CharField(max_length=100,blank=True,null=True,default=None)
    user_profile=models.ImageField(upload_to='profile_images',blank=True,null=True)
