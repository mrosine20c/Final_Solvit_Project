from django.db import models

# Create your models here.

class DjangoModel(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(verbose_name="content")
    progress=models.BooleanField()
    
    def __str__(self):
        return self.title

class Node(models.Model):
    title = models.CharField(max_length=140 ,verbose_name="node")
    content = models.TextField(verbose_name="content")
    progress = models.BooleanField()  

    def __str__ (self):
        return self.title 
    
class React(models.Model):
    title= models.CharField(max_length=140 ,verbose_name="node")
    content = models.TextField(verbose_name="content")
    progress = models.BooleanField()

    def __str__ (self):
        return self.title

class Ui_ux(models.Model):
    title = models.CharField(max_length=140,verbose_name="ui")
    content = models.TextField(verbose_name="content")
    progress = models.BooleanField()

    def __str__ (self):
        return self.title

class Laravel(models.Model):
    title = models.CharField(max_length=40,verbose_name="laravel")
    content = models.TextField(verbose_name="content")
    progress = models.BooleanField()

    def __str__ (self):
        return self.title
         
    