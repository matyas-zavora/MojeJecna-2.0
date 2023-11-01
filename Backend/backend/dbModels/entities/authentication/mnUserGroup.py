from django.db import models

class MnUserGroup(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    
    #FK
    user = models.ForeignKey("dbModels.user", on_delete=models.CASCADE)
    group = models.ForeignKey("dbModels.group", on_delete=models.CASCADE)