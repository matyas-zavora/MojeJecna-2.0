from django.db import models

class Group(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    #common informations
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(max_length=800, blank=True, null=True)
    code = models.CharField(max_length=4)
    
    def __str__(self) -> str:
        return self.name