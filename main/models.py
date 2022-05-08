#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class yonghu(BaseModel):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='gerenzhanghao'


    __authTables__={}
    __authPeople__='yes'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='gerenzhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='no'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='no'#后台列表权限
    __thumbsUp__='no'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='no'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='no'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='no'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='no'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='no'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'create time')
    gerenzhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='personal account' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='password' )
    xingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='name' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='gender' )
    youxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='email' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='phone number' )
    touxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='head portrait' )
    money=models.FloatField   (  null=True, unique=False,default='0', verbose_name='remaining' )
    '''
    gerenzhanghao=VARCHAR
    mima=VARCHAR
    xingming=VARCHAR
    xingbie=VARCHAR
    youxiang=VARCHAR
    shoujihaoma=VARCHAR
    touxiang=VARCHAR
    money=Float
    '''
    class Meta:
        db_table = 'yonghu'
        verbose_name = verbose_name_plural = 'user'
class shangpinxinxi(BaseModel):
    __doc__ = u'''shangpinxinxi'''
    __tablename__ = 'shangpinxinxi'



    __authTables__={}
    __authPeople__='no'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='no'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='no'#后台列表权限
    __thumbsUp__='no'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='yes'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='yes'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='no'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='yes'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='no'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'create time')
    shangpinmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='product name' )
    shangpinleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='product type' )
    shangpintupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='product picture' )
    shangpinjianjie=models.TextField   (  null=True, unique=False, verbose_name='Product introduction' )
    shangpinguige=models.CharField ( max_length=255, null=True, unique=False, verbose_name='commercial specification' )
    shangpinxiangqing=models.TextField   (  null=True, unique=False, verbose_name='commodity details' )
    shengchandi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='yieldly' )
    yuancailiao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='raw material' )
    shangjiariqi=models.DateField   (  null=True, unique=False, verbose_name='Date Added' )
    clicktime=models.DateTimeField  (  null=True, unique=False, verbose_name='Last click time' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='click times' )
    price=models.FloatField   (  null=True, unique=False, verbose_name='Price' )
    '''
    shangpinmingcheng=VARCHAR
    shangpinleixing=VARCHAR
    shangpintupian=VARCHAR
    shangpinjianjie=Text
    shangpinguige=VARCHAR
    shangpinxiangqing=Text
    shengchandi=VARCHAR
    yuancailiao=VARCHAR
    shangjiariqi=Date
    clicktime=DateTime
    clicknum=Integer
    price=Float
    '''
    class Meta:
        db_table = 'shangpinxinxi'
        verbose_name = verbose_name_plural = 'merchandise news'
class shangpinleixing(BaseModel):
    __doc__ = u'''shangpinleixing'''
    __tablename__ = 'shangpinleixing'



    __authTables__={}
    __authPeople__='no'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='no'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='no'#后台列表权限
    __thumbsUp__='no'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='no'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='no'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='no'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='no'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='no'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'create time')
    shangpinleixing=models.CharField ( max_length=255,null=False, unique=False, verbose_name='product type' )
    '''
    shangpinleixing=VARCHAR
    '''
    class Meta:
        db_table = 'shangpinleixing'
        verbose_name = verbose_name_plural = 'product type'
class cart(BaseModel):
    __doc__ = u'''cart'''
    __tablename__ = 'cart'



    __authTables__={}
    __authSeparate__='yes'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'create time')
    tablename=models.CharField ( max_length=255, null=True, unique=False,default='shangpinxinxi', verbose_name='product table name' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='user id' )
    goodid=models.BigIntegerField  ( null=False, unique=False, verbose_name='product id' )
    goodname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='product name' )
    picture=models.CharField ( max_length=255, null=True, unique=False, verbose_name='picture' )
    buynumber=models.IntegerField  ( null=False, unique=False, verbose_name='quantity' )
    price=models.FloatField   (  null=True, unique=False, verbose_name='unit price' )
    discountprice=models.FloatField   (  null=True, unique=False, verbose_name='VIP price' )
    '''
    tablename=VARCHAR
    userid=BigInteger
    goodid=BigInteger
    goodname=VARCHAR
    picture=VARCHAR
    buynumber=Integer
    price=Float
    discountprice=Float
    '''
    class Meta:
        db_table = 'cart'
        verbose_name = verbose_name_plural = 'cart table'
class orders(BaseModel):
    __doc__ = u'''orders'''
    __tablename__ = 'orders'



    __authTables__={}
    __authSeparate__='yes'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'create time')
    orderid=models.CharField ( max_length=255,null=False,unique=True, verbose_name='order number' )
    tablename=models.CharField ( max_length=255, null=True, unique=False,default='shangpinxinxi', verbose_name='product table name' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='user id' )
    goodid=models.BigIntegerField  ( null=False, unique=False, verbose_name='product id' )
    goodname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='product name' )
    picture=models.CharField ( max_length=255, null=True, unique=False, verbose_name='product picture' )
    buynumber=models.IntegerField  ( null=False, unique=False, verbose_name='quantity' )
    price=models.FloatField   ( null=False, unique=False,default='0', verbose_name='price' )
    discountprice=models.FloatField   (  null=True, unique=False,default='0', verbose_name='discounted price' )
    total=models.FloatField   ( null=False, unique=False,default='0', verbose_name='total price' )
    discounttotal=models.FloatField   (  null=True, unique=False,default='0', verbose_name='Total discount price' )
    type=models.IntegerField  (  null=True, unique=False,default='1', verbose_name='type of payment' )
    status=models.CharField ( max_length=255, null=True, unique=False, verbose_name='state' )
    address=models.CharField ( max_length=255, null=True, unique=False, verbose_name='address' )
    tel=models.CharField ( max_length=255, null=True, unique=False, verbose_name='phone number' )
    consignee=models.CharField ( max_length=255, null=True, unique=False, verbose_name='consignee' )
    logistics=models.TextField   (  null=True, unique=False, verbose_name='logistics' )
    '''
    orderid=VARCHAR
    tablename=VARCHAR
    userid=BigInteger
    goodid=BigInteger
    goodname=VARCHAR
    picture=VARCHAR
    buynumber=Integer
    price=Float
    discountprice=Float
    total=Float
    discounttotal=Float
    type=Integer
    status=VARCHAR
    address=VARCHAR
    tel=VARCHAR
    consignee=VARCHAR
    logistics=Text
    '''
    class Meta:
        db_table = 'orders'
        verbose_name = verbose_name_plural = 'order'
class address(BaseModel):
    __doc__ = u'''address'''
    __tablename__ = 'address'



    __authTables__={}
    __authSeparate__='yes'#后台列表权限
    __foreEndListAuth__='yes'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'create time')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='user id' )
    address=models.CharField ( max_length=255,null=False, unique=False, verbose_name='address' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='consignee ' )
    phone=models.CharField ( max_length=255,null=False, unique=False, verbose_name='phone number' )
    isdefault=models.CharField ( max_length=255,null=False, unique=False, verbose_name='Default address [Yes/No]' )
    '''
    userid=BigInteger
    address=VARCHAR
    name=VARCHAR
    phone=VARCHAR
    isdefault=VARCHAR
    '''
    class Meta:
        db_table = 'address'
        verbose_name = verbose_name_plural = 'address'
class storeup(BaseModel):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='yes'#后台列表权限
    __foreEndListAuth__='yes'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'create time')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='user id' )
    refid=models.BigIntegerField  (  null=True, unique=False, verbose_name='collect id' )
    tablename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='table name' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='collection name' )
    picture=models.CharField ( max_length=255,null=False, unique=False, verbose_name='collection picture' )
    type=models.CharField ( max_length=255, null=True, unique=False,default='1', verbose_name='type(1:collect,21:like,22:dislike)' )
    inteltype=models.CharField ( max_length=255, null=True, unique=False, verbose_name='Recommend type' )
    '''
    userid=BigInteger
    refid=BigInteger
    tablename=VARCHAR
    name=VARCHAR
    picture=VARCHAR
    type=VARCHAR
    inteltype=VARCHAR
    '''
    class Meta:
        db_table = 'storeup'
        verbose_name = verbose_name_plural = 'collection table'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'create time')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='title' )
    introduction=models.TextField   (  null=True, unique=False, verbose_name='introduction' )
    picture=models.CharField ( max_length=255,null=False, unique=False, verbose_name='picture' )
    content=models.TextField   ( null=False, unique=False, verbose_name='content' )
    '''
    title=VARCHAR
    introduction=Text
    picture=VARCHAR
    content=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = 'announcement information'
class discussshangpinxinxi(BaseModel):
    __doc__ = u'''discussshangpinxinxi'''
    __tablename__ = 'discussshangpinxinxi'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'create time')
    refid=models.BigIntegerField  ( null=False, unique=False, verbose_name='association table id' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='user id' )
    nickname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='user name' )
    content=models.TextField   ( null=False, unique=False, verbose_name='comment content' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='response' )
    '''
    refid=BigInteger
    userid=BigInteger
    nickname=VARCHAR
    content=Text
    reply=Text
    '''
    class Meta:
        db_table = 'discussshangpinxinxi'
        verbose_name = verbose_name_plural = 'Product information review form'
