from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserInfo(AbstractUser):
    phone = models.CharField(max_length=32, verbose_name="手机号", null=True, blank=True)
    """
    null=True 数据库可以为空
    blank=True 后台管理可以为空
    """

    create_time = models.DateField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "用户表"


class Article(models.Model):
    title = models.CharField(verbose_name="文章标题", max_length=64)
    desc = models.CharField(verbose_name="文章简介", max_length=255)
    # 文章内容有很多，一般情况下都是使用TextFiled()
    content = models.TextField(verbose_name="文章内容")

    create_time = models.DateField(auto_now_add=True, verbose_name="创建时间")
