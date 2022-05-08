# coding:utf-8
__author__ = "ila"

from django.db import models

from .model import BaseModel


class users(BaseModel):
    # id=models.BigIntegerField(verbose_name="自增id")
    username = models.CharField(max_length=100, verbose_name=u'account')
    password = models.CharField(max_length=100, verbose_name=u'password')
    role = models.CharField(max_length=100, verbose_name=u'character')
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'create time')
    __tablename__ = 'users'

    class Meta:
        db_table = 'users'
        verbose_name = verbose_name_plural = u'admin table'

    # def __str__(self):
    #     return self.username
