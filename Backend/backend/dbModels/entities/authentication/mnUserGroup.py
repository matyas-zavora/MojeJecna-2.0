from django.db import models

class MnUserGroup(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    id_user = models.ForeignKey("dbModels.user", on_delete=models.CASCADE)
    id_group = models.ForeignKey("dbModels.group", on_delete=models.CASCADE)