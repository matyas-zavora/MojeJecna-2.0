from django.contrib import admin
from dbModels.models import DjangoUser
from dbModels.entities.authentication.user import User
from dbModels.entities.authentication.group import Group
from dbModels.entities.authentication.mnUserGroup import MnUserGroup

# Register your models here.
admin.site.register(DjangoUser)
admin.site.register(User)
admin.site.register(Group)
admin.site.register(MnUserGroup)