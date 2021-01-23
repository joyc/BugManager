from django.db import models


# Create your models here.
class UserInfo(models.Model):
    """用户信息表"""
    # id = models.IntegerField(primary_key=True)    # 自动会加
    login_name = models.CharField(verbose_name="登录名", max_length=100, db_index=True)    # 登录名字段
    username = models.CharField(verbose_name="姓名", max_length=100)  # 姓名
    email = models.EmailField(verbose_name="邮箱", max_length=200)    # 邮箱
    mobile = models.CharField(verbose_name="手机号码", max_length=100)    # 手机号码
    password = models.CharField(verbose_name="密码", max_length=300)  # 密码

    class Meta:
        managed = True
        # db_table = ""

    def __str__(self):
        return f"登录名：{self.login_name} \t 用户名：{self.username}"
