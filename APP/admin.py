from django.contrib import admin
from . models import UserPersonalModel, ImageModel
# Register your models here.


admin.site.register(UserPersonalModel)
admin.site.register(ImageModel)