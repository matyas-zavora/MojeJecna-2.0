from django.contrib import admin
from dbModels.models import DjangoUser
from dbModels.entities.user import User

# Register your models here.
admin.site.register(DjangoUser)
admin.site.register(User)