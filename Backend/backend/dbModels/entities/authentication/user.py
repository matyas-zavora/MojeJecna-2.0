from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    #common informations
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(blank=True, null=True, unique=True)
    
    #personal infomations
    first_name = models.CharField(blank=False, null=False, max_length=150)
    middle_name = models.CharField(blank=True, null=True, max_length=150)
    last_name = models.CharField(blank=False, null=False, max_length=150)
    
    #school info
    user_type = models.ForeignKey('UserType', on_delete=models.CASCADE)
    user_class = models.ForeignKey('UserClass',blank=True, null=True, on_delete=models.SET_NULL)
    education_group = models.ForeignKey('EducationGroup',blank=True, null=True, on_delete=models.SET_NULL)
    
    def __str__(self) -> str:
        return self.username
    
    def get_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "name":{
                "first_name": self.first_name,
                "middle_name": self.middle_name,
                "last_name": self.last_name,
            },
            "user_type_id": self.user_type.id,
            "user_class_id": self.user_class.id if self.user_class else None,
            "education_group_id": self.education_group.id if self.education_group else None
        }