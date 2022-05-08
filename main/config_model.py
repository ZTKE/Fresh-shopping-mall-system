# coding:utf-8
__author__ = "ila"

from django.db import models

from .model import BaseModel


class config(BaseModel):
    # id=models.BigIntegerField(verbose_name="自增id")
    name = models.CharField(max_length=100, verbose_name=u'key name')
    value = models.CharField(max_length=100, verbose_name=u'key value')

    __tablename__ = 'config'

    class Meta:
        db_table = 'config'
        verbose_name = verbose_name_plural = u'configuration table'

    # def __str__(self):
    #     return self.name
