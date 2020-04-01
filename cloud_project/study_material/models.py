from django.db import models

# Create your models here.


class gate_privious_year(models.Model):
    course_name=models.CharField(max_length=100,blank=True,null=True)
    course_catagery=models.CharField(max_length=100,blank=True,null=True)
    Year_of_question_paper=models.CharField(max_length=100,blank=True,null=True)
    question_paper=models.FileField(upload_to='Gate_material/',blank=True,null=True)
    answer_key=models.FileField(upload_to='Gate_material/',blank=True,null=True)


class online_mock_test(models.Model):
    course_name=models.CharField(max_length=100,blank=True,null=True)
    course_catagery=models.CharField(max_length=100,blank=True,null=True)
    mock_test_url=models.CharField(max_length=100,blank=True,null=True)
