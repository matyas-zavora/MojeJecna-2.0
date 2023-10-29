from django.db import models

class EducationGroup(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name