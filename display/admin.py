from django.contrib import admin
#从本级目录导入模块(.models)
from .models import Display

# Register your models here.
#注册模块

admin.site.register(Display)