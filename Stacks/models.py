from django.db import models

# Create your models here.
class DjangoModel(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(verbose_name="content")
    progress=models.BooleanField
    
    def __str__(self):
        return self.title
    