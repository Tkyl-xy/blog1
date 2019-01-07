from django.db import models

# Create your models here.
#实现组件的功能

class Display(models.Model):
    # 文本描述的属性,default是默认的属性
    description = models.CharField(default='在这里写作品的简介',max_length=100)
    #图片模型,uploade_to="这里面是图片路径", upload_to是上传的意思,图片路径为images/
    image = models.ImageField(default='default.png', upload_to='images/')
    title = models.CharField(default="作品标题",max_length=50)

    #这里是实现管理标题，便于管理以后的描述标题
    def __str__(self):
    	return self.title
'''
class MODELNAME(models.Model):

    class Meta:
        verbose_name = "MODELNAME"
        verbose_name_plural = "MODELNAMEs"

    def __str__(self):
        pass
'''