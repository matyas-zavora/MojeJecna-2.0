from django.contrib import admin
from dbModels.models import DjangoUser
from dbModels.entities.authentication.user import User
from dbModels.entities.authentication.group import Group
from dbModels.entities.authentication.mnUserGroup import MnUserGroup
from dbModels.entities.authentication.userType import UserType
admin.site.register(UserType)
admin.site.register(DjangoUser)
admin.site.register(User)
admin.site.register(Group)
admin.site.register(MnUserGroup)

from dbModels.entities.school.educationGroup import EducationGroup
from dbModels.entities.school.userClass import UserClass
admin.site.register(EducationGroup)
admin.site.register(UserClass)


# Register your models here.