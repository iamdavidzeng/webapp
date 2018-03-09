from django.db import models

# Create your models here.


class UserProfile(models.Model):
    first_name = models.CharField(verbose_name='姓', max_length=5)
    last_name = models.CharField(verbose_name='名', max_length=5)
    birth = models.DateField(verbose_name='生日', null=True)
    phone = models.CharField(verbose_name='手机', max_length=11, null=True)
    email = models.EmailField(verbose_name='邮箱', null=True)

    class Meta:
        db_table = 't_users_info'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
