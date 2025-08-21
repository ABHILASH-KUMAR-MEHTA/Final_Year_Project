from django.db import models
from embed_video.fields import EmbedVideoField











# Create your models here.
class mysoftware(models.Model):
    software_title=models.CharField(max_length=100, null=True)
    software_description=models.TextField( null=True)
    software_picture=models.ImageField(upload_to='static/softwarepic/', null=True)
    software_date=models.DateField()

class category(models.Model):
    category_name=models.CharField(max_length=200,null=True)
    category_picture=models.ImageField(upload_to='static/category',null=True)
    category_date=models.DateField()
    def __str__(self):
        return self.category_name



class studentbatch(models.Model):
    batch_name=models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.batch_name

class mylectures(models.Model):
    video_category=models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    video_batch=models.ForeignKey(studentbatch, on_delete=models.CASCADE,null=True)
    vlink=models.CharField(max_length=300, null=True)
    thumbnail=models.ImageField(upload_to='static/video', null=True)
    video_description=models.TextField(null=True)
    added_date=models.DateField()

class batchtiming(models.Model):
    batch=models.ForeignKey(studentbatch, on_delete=models.CASCADE, null=True)
    clink=models.CharField(max_length=300, null=True)
    timing=models.CharField(max_length=50, null=True)
    start_date=models.DateField()

class Item(models.Model):
    video=EmbedVideoField()
class Item1(models.Model):
    therapy=EmbedVideoField()