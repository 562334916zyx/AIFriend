import uuid

from django.db import models
from django.utils.timezone import now, localtime

from web.models.user import UserProfile

#定义一个函数用来动态生成头像的名字
def photo_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4().hex[:10]}.{ext}'#随机字符串的长度降到10
    return f'character/photos/{instance.author.user_id}_{filename}'


#定义一个函数用来动态生成聊天背景的名字
def background_image_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4().hex[:10]}.{ext}'#随机字符串的长度降到10
    return f'character/background_images/{instance.author.user_id}_{filename}'


#创建一个数据库
class Character(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)#每个角色是谁创建的
    name = models.CharField(max_length=50)#创建一个名字
    photo = models.ImageField(upload_to=photo_upload_to)#定义一个头像
    profile = models.TextField(max_length=100000)#定义一个简介
    background_image = models.ImageField(upload_to=background_image_upload_to)
    create_time = models.DateTimeField(default=now)

    def __str__(self):
      return f"{self.author.user.username} - {self.name} - {localtime(self.create_time).strftime('%Y-%m-%d %H:%M:%S')}"