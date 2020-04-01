from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.
class institute_information(models.Model):
    institute_name=models.CharField(max_length=100,blank=True,null=True)
    user_id=models.IntegerField(default=None)
    institute_email=models.CharField(max_length=100,blank=True,null=True)
    address=models.CharField(max_length=100,blank=True,null=True)
    address2=models.CharField(max_length=100,blank=True,null=True)
    city=models.CharField(max_length=150,blank=True,null=True)
    district=models.CharField(max_length=100,blank=True,null=True)
    state=models.CharField(max_length=100,blank=True,null=True)
    zip_code=models.CharField(max_length=50,blank=True,null=True)
    institute_mobile_no=models.CharField(max_length=13,blank=True,null=True)
    institute_mobile_no2=models.CharField(max_length=13,blank=True,null=True)
    institute_description=models.TextField(max_length=300,blank=True,null=True)
    institute_logo=models.ImageField(upload_to="institute_logo/",blank=True,null=True)



class course_detail(models.Model):
    institute=models.ForeignKey(institute_information, on_delete=models.CASCADE)
    inst_id=models.IntegerField()
    course_name=models.CharField(max_length=100,blank=True,null=True)
    course_catagery=models.CharField(max_length=100,blank=True,null=True)
    cousrse_fees=models.CharField(max_length=50)



class faculty_detail(models.Model):
    #institute=models.ForeignKey(institute_information, on_delete=models.CASCADE)
    inst_id=models.IntegerField()
    faculty_name=models.CharField(max_length=50,blank=True,null=True)
    faculty_email=models.CharField(max_length=100,blank=True,null=True)
    faculty_image=models.ImageField(upload_to='faculty_image/',max_length=100,blank=True,null=True)
    desc_faculty_edu=models.CharField(max_length=100,blank=True,null=True)
    faculty_description_experience=models.CharField(max_length=300,blank=True,null=True)



class Images(models.Model):
    institute=models.ForeignKey(institute_information, on_delete=models.CASCADE)
    inst_id=models.IntegerField()
    institute_photos=models.ImageField(upload_to='institute_images/',default="http://dummyimage.com/60x60/666/ffffff&text=No+Image")

class institute_result(models.Model):
    institute=models.ForeignKey(institute_information, on_delete=models.CASCADE)
    inst_id=models.IntegerField()
    institute_result=models.ImageField(upload_to='institute_result/',default="http://dummyimage.com/60x60/666/ffffff&text=No+Image")

class Inst_review(models.Model):
    institute=models.ForeignKey(institute_information, on_delete=models.CASCADE)
    inst_id=models.IntegerField()
    user_id=models.IntegerField()
    review=models.TextField(max_length=300,blank=True,null=False)
    date = models.DateTimeField(auto_now=True,max_length=50, blank=True,null=True)
    review_star=models.IntegerField(default=None)


class rating_detail(models.Model):
    institute=models.ForeignKey(institute_information, on_delete=models.CASCADE)
    inst_id=models.IntegerField()
    average_rating=models.FloatField(default=0)
