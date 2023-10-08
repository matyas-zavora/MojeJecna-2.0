from django.db import models

class User(models):
    id = models.AutoField(primary_key=True, auto_created=True)
    #common informations
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=256)
    #email = models.EmailField(blank=True, null=True, unique=True)
    #
    ##personal infomations
    #first_name = models.CharField(blank=False, null=False, max_length=150)
    #middle_name = models.CharField(blank=True, null=True, max_length=150)
    #last_name = models.CharField(blank=False, null=False, max_length=150)
    
    #school info