from django.contrib import admin

from module.models import UserModel, NotesModel
# from models import *
# Register your models here.


admin.site.register(UserModel)
admin.site.register(NotesModel)