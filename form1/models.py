from django.db import models

# Create your models here.
class personalinfo(models.Model):
    name=models.CharField(max_length=50)
    discription=models.TextField(max_length=100)
    
    class Meta:
        verbose_name_plural="personal information"
        
    def __str__(self):
        return f'{self.name} , {self.discription}'