from django.db import models

# Create your models here.
class contactus(models.Model):
    name=models.CharField(max_length=200,null=True)
    mobile=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=200,null=True)
    message=models.TextField(null=True)
    def __str__(self):
        return self.name
class slider(models.Model):
    headlines=models.TextField()
    slider_dec=models.TextField()
    slider_picture=models.ImageField(upload_to='static/slider/',null=True)
    def __str__(self):
        return self.headlines
class newbatches(models.Model):
    name=models.CharField(max_length=100)
    batch_pic=models.ImageField(upload_to='static/newbatches/',null=True)
    starting_date=models.DateTimeField()


class college(models.Model):
    college_name=models.CharField(max_length=200, null=True)
    college_picture=models.ImageField(upload_to='static/college/',null=True)
    def __str__(self):
        return self.college_name

class session_year(models.Model):
    session=models.CharField(max_length=1000)
    def __str__(self):
        return self.session

class batch(models.Model):
    batch_name=models.CharField(max_length=50)
    def __str__(self):
        return self.batch_name

class placement(models.Model):
    student_picture=models.ImageField(upload_to='static/placement/',null=True)
    student_name=models.CharField(max_length=100,null=True)
    college=models.ForeignKey(college,on_delete=models.CASCADE)
    session=models.ForeignKey(session_year,on_delete=models.CASCADE)
    batch=models.ForeignKey(batch,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=200,null=True)
    company_logo=models.ImageField(upload_to='static/company',null=True)

class registration(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,primary_key=True)
    mobile=models.CharField(max_length=30,null=True)
    profile=models.ImageField(upload_to='static/profile/',null=True)
    course=models.CharField(max_length=30,null=True)
    pyear=models.CharField(max_length=30,null=True)
    college=models.CharField(max_length=200,null=True)
    batch=models.CharField(max_length=40,null=True)
    status=models.CharField(max_length=30,null=True)
    passwd=models.CharField(max_length=100,null=True)
    batchid = models.IntegerField(null=True)


    def __str__(self):
        return self.name





