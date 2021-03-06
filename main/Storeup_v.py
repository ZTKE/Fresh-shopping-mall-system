#coding:utf-8
__author__ = "ila"
import base64, copy, logging, os, time, xlrd
from django.http import JsonResponse
from django.apps import apps
from django.db.models.aggregates import Count,Sum
from .models import storeup
from util.codes import *
from util.auth import Auth
from util.common import Common
import util.message as mes
from django.db import connection
import random
from django.core.mail import send_mail
from alipay import AliPayConfig, AliPay
from django.conf import settings
from django.shortcuts import redirect

def storeup_register(request):
    if request.method in ["POST", "GET"]:
        msg = {'code': normal_code, "msg": mes.normal_code}
        req_dict = request.session.get("req_dict")


        error = storeup.createbyreq(storeup, storeup, req_dict)
        if error != None:
            msg['code'] = crud_error_code
            msg['msg'] = "Please do not register again!"
        return JsonResponse(msg)

def storeup_login(request):
    if request.method in ["POST", "GET"]:
        msg = {'code': normal_code, "msg": mes.normal_code}
        req_dict = request.session.get("req_dict")

        datas = storeup.getbyparams(storeup, storeup, req_dict)
        if not datas:
            msg['code'] = password_error_code
            msg['msg'] = mes.password_error_code
            return JsonResponse(msg)
        try:
            __sfsh__= storeup.__sfsh__
        except:
            __sfsh__=None

        if  __sfsh__=='yes':
            if datas[0].get('sfsh')=='no':
                msg['code']=other_code
                msg['msg'] = "Account has been locked, please contact the administrator to review!"
                return JsonResponse(msg)
                
        req_dict['id'] = datas[0].get('id')
        return Auth.authenticate(Auth, storeup, req_dict)


def storeup_logout(request):
    if request.method in ["POST", "GET"]:
        msg = {
            "msg": "logout successfully",
            "code": 0
        }

        return JsonResponse(msg)


def storeup_resetPass(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code}

        req_dict = request.session.get("req_dict")

        columns=  storeup.getallcolumn( storeup, storeup)

        try:
            __loginUserColumn__= storeup.__loginUserColumn__
        except:
            __loginUserColumn__=None
        username=req_dict.get(list(req_dict.keys())[0])
        if __loginUserColumn__:
            username_str=__loginUserColumn__
        else:
            username_str=username
        if 'mima' in columns:
            password_str='mima'
        else:
            password_str='password'

        init_pwd = '123456'

        eval('''storeup.objects.filter({}='{}').update({}='{}')'''.format(username_str,username,password_str,init_pwd))
        
        return JsonResponse(msg)



def storeup_session(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code,"msg": mes.normal_code, "data": {}}

        req_dict={"id":request.session.get('params').get("id")}
        msg['data']  = storeup.getbyparams(storeup, storeup, req_dict)[0]

        return JsonResponse(msg)


def storeup_default(request):

    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code,"msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        req_dict.update({"isdefault":"yes"})
        data=storeup.getbyparams(storeup, storeup, req_dict)
        if len(data)>0:
            msg['data']  = data[0]
        else:
            msg['data']  = {}
        return JsonResponse(msg)

def storeup_page(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")

        #??????????????????
        columns=  storeup.getallcolumn( storeup, storeup)

        #???????????????????????????
        tablename = request.session.get("tablename")


            #authColumn=list(__authTables__.keys())[0]
            #authTable=__authTables__.get(authColumn)

            # if authTable==tablename:
                #params = request.session.get("params")
                #req_dict[authColumn]=params.get(authColumn)

        '''__authSeparate__??????????????????params??????userid??????????????????????????????'''
        try:
            __authSeparate__=storeup.__authSeparate__
        except:
            __authSeparate__=None

        if __authSeparate__=="yes":
            tablename=request.session.get("tablename")
            if tablename!="users" and 'userid' in columns:
                try:
                    req_dict['userid']=request.session.get("params").get("id")
                except:
                    pass

        #???????????????hasMessage??????????????????????????????????????????????????????messages???????????????????????????hasMessage????????????????????????,????????????userid?????????id??????username(?????????)???content?????????????????????reply????????????
        #??????page?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
        try:
            __hasMessage__=storeup.__hasMessage__
        except:
            __hasMessage__=None
        if  __hasMessage__=="yes":
            tablename=request.session.get("tablename")
            if tablename!="users":
                req_dict["userid"]=request.session.get("params").get("id")



        # ???????????????????????????isAdmin,????????????????????????
        # ????????????isAdmin=?????????,??????????????????????????????????????????page???list????????????????????????????????????(????????????????????????)
        __isAdmin__ = None

        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__==tablename:

                try:
                    __isAdmin__ = m.__isAdmin__
                except:
                    __isAdmin__ = None
                break

        # ???????????????????????????????????????
        if  __isAdmin__ == "yes":
            if req_dict.get("userid"):
                del req_dict["userid"]

        else:
            #????????????????????????,?????????????????????????????????userid
            if tablename!="users" and 'storeup'[:7]!='discuss'and "userid" in storeup.getallcolumn(storeup,storeup):
                req_dict["userid"] = request.session.get("params").get("id")

        #????????????authTable??????(???????????????)[????????????????????????????????????????????????????????????]????????????????????????????????????authTable???????????????????????????????????????????????????????????????????????????
        try:
            __authTables__=storeup.__authTables__
        except:
            __authTables__=None

        if __authTables__!=None and  __authTables__!={}:
            try:
                del req_dict['userid']
            except:
                pass
            for authColumn,authTable in __authTables__.items():
                if authTable==tablename:
                    params = request.session.get("params")
                    req_dict[authColumn]=params.get(authColumn)
                    break
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  =storeup.page(storeup, storeup, req_dict)

        return JsonResponse(msg)

def storeup_autoSort(request):
    '''
    ?????????????????????(????????????[intelRecom??????/??????],??????clicktime[????????????????????????]???????????????info/detail??????????????????????????????clicktime????????????)
?????????????????????????????????????????????????????????????????????????????????????????????????????????5???????????????
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")
        if "clicknum"  in storeup.getallcolumn(storeup,storeup):
            req_dict['sort']='clicknum'
        else:
            req_dict['sort']='clicktime'
        req_dict['order']='desc'
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = storeup.page(storeup,storeup, req_dict)

        return JsonResponse(msg)


def storeup_list(request):
    '''
    ????????????
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")

        #??????????????????
        columns=  storeup.getallcolumn( storeup, storeup)
        #?????????[foreEndList]??????list:??????????????????list???????????????,??????????????????,???:???????????????,???:???????????????(???????????????????????????),?????????:?????????????????????????????????????????????
        try:
            __foreEndList__=storeup.__foreEndList__
        except:
            __foreEndList__=None

        if __foreEndList__=="Before boarding":
            tablename=request.session.get("tablename")
            if tablename!="users" and 'userid' in columns:
                try:
                    req_dict['userid']=request.session.get("params").get("id")
                except:
                    pass
        #forrEndListAuth
        try:
            __foreEndListAuth__=storeup.__foreEndListAuth__
        except:
            __foreEndListAuth__=None


        #authSeparate
        try:
            __authSeparate__=storeup.__authSeparate__
        except:
            __authSeparate__=None

        if __foreEndListAuth__ =="yes" and __authSeparate__=="yes":
            tablename=request.session.get("tablename")
            if tablename!="users":
                req_dict['userid']=request.session.get("params",{"id":0}).get("id")

        tablename = request.session.get("tablename")
        if tablename == "users" and req_dict.get("userid") != None:#??????????????????userid??????
            del req_dict["userid"]
        else:
            __isAdmin__ = None

            allModels = apps.get_app_config('main').get_models()
            for m in allModels:
                if m.__tablename__==tablename:

                    try:
                        __isAdmin__ = m.__isAdmin__
                    except:
                        __isAdmin__ = None
                    break

            if __isAdmin__ == "yes":
                if req_dict.get("userid"):
                    del req_dict["userid"]
            else:
                #????????????????????????,?????????????????????????????????userid
                if "userid" in columns:
                    try:
                        # ???????????????????????????,??????try?????????????????????
                        req_dict['userid']=request.session.get("params").get("id")
                    except:
                            pass
        #????????????authTable??????(???????????????)[????????????????????????????????????????????????????????????]????????????????????????????????????authTable???????????????????????????????????????????????????????????????????????????
        try:
            __authTables__=storeup.__authTables__
        except:
            __authTables__=None

        if __authTables__!=None and  __authTables__!={} and __foreEndListAuth__=="yes":
            try:
                del req_dict['userid']
            except:
                pass
            for authColumn,authTable in __authTables__.items():
                if authTable==tablename:
                    params = request.session.get("params")
                    req_dict[authColumn]=params.get(authColumn)
                    break
        
        if storeup.__tablename__[:7]=="discuss":
            try:
                del req_dict['userid']
            except:
                pass


        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = storeup.page(storeup, storeup, req_dict)

        return JsonResponse(msg)

def storeup_save(request):
    '''
    ????????????
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        tablename=request.session.get("tablename")
        __isAdmin__ = None
        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__==tablename:

                try:
                    __isAdmin__ = m.__isAdmin__
                except:
                    __isAdmin__ = None
                break


        #??????????????????
        columns=  storeup.getallcolumn( storeup, storeup)
        if tablename!='users' and req_dict.get("userid")!=None and 'userid' in columns  and __isAdmin__!='yes':
            params=request.session.get("params")
            req_dict['userid']=params.get('id')


        error= storeup.createbyreq(storeup,storeup, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error

        return JsonResponse(msg)


def storeup_add(request):
    '''
    ????????????
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")

        #??????????????????
        columns=  storeup.getallcolumn( storeup, storeup)
        try:
            __authSeparate__=storeup.__authSeparate__
        except:
            __authSeparate__=None

        if __authSeparate__=="yes":
            tablename=request.session.get("tablename")
            if tablename!="users" and 'userid' in columns:
                try:
                    req_dict['userid']=request.session.get("params").get("id")
                except:
                    pass

        try:
            __foreEndListAuth__=storeup.__foreEndListAuth__
        except:
            __foreEndListAuth__=None

        if __foreEndListAuth__ and __foreEndListAuth__!="no":
            tablename=request.session.get("tablename")
            if tablename!="users":
                req_dict['userid']=request.session.get("params").get("id")

        error= storeup.createbyreq(storeup,storeup, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg)

def storeup_thumbsup(request,id_):
    '''
     ??????????????????thumbsUp[???/???]???????????????thumbsupnum??????crazilynum????????????
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        id_=int(id_)
        type_=int(req_dict.get("type",0))
        rets=storeup.getbyid(storeup,storeup,id_)

        update_dict={
        "id":id_,
        }
        if type_==1:#???
            update_dict["thumbsupnum"]=int(rets[0].get('thumbsupnum'))+1
        elif type_==2:#???
            update_dict["crazilynum"]=int(rets[0].get('crazilynum'))+1
        error = storeup.updatebyparams(storeup,storeup, update_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg)


def storeup_info(request,id_):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}

        data = storeup.getbyid(storeup,storeup, int(id_))
        if len(data)>0:
            msg['data']=data[0]
        #??????????????????
        try:
            __browseClick__= storeup.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__=="yes"  and  "clicknum"  in storeup.getallcolumn(storeup,storeup):
            try:
                clicknum=int(data[0].get("clicknum",0))+1
            except:
                clicknum=0+1
            click_dict={"id":int(id_),"clicknum":clicknum}
            ret=storeup.updatebyparams(storeup,storeup,click_dict)
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return JsonResponse(msg)

def storeup_detail(request,id_):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}

        data =storeup.getbyid(storeup,storeup, int(id_))
        if len(data)>0:
            msg['data']=data[0]

        #??????????????????
        try:
            __browseClick__= storeup.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__=="yes"   and  "clicknum"  in storeup.getallcolumn(storeup,storeup):
            try:
                clicknum=int(data[0].get("clicknum",0))+1
            except:
                clicknum=0+1
            click_dict={"id":int(id_),"clicknum":clicknum}

            ret=storeup.updatebyparams(storeup,storeup,click_dict)
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = retfo
        return JsonResponse(msg)


def storeup_update(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        if req_dict.get("mima") and req_dict.get("password"):
            if "mima" not  in storeup.getallcolumn(storeup,storeup) :
                del req_dict["mima"]
            if  "password" not  in storeup.getallcolumn(storeup,storeup) :
                del req_dict["password"]
        try:
            del req_dict["clicknum"]
        except:
            pass


        error = storeup.updatebyparams(storeup, storeup, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg)


def storeup_delete(request):
    '''
    ????????????
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")

        error=storeup.deletes(storeup,
            storeup,
             req_dict.get("ids")
        )
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg)


def storeup_vote(request,id_):
    '''
    ??????????????????????????????[browseClick:???/???]??????????????????clicknum????????????info/detail???????????????????????????+1??????????????????????????????[vote:???/???]??????????????????votenum???,??????vote????????????votenum+1???
??????????????????????????????????????????????????????????????????
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code}


        data= storeup.getbyid(storeup, storeup, int(id_))
        for i in data:
            votenum=i.get('votenum')
            if votenum!=None:
                params={"id":int(id_),"votenum":votenum+1}
                error=storeup.updatebyparams(storeup,storeup,params)
                if error!=None:
                    msg['code'] = crud_error_code
                    msg['msg'] = error
        return JsonResponse(msg)

def storeup_importExcel(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "success", "data": {}}

        excel_file = request.FILES.get("file", "")
        file_type = excel_file.name.split('.')[1]
        
        if file_type in ['xlsx', 'xls']:
            data = xlrd.open_workbook(filename=None, file_contents=excel_file.read())
            table = data.sheets()[0]
            rows = table.nrows
            
            try:
                for row in range(1, rows):
                    row_values = table.row_values(row)
                    req_dict = {}
                    storeup.createbyreq(storeup, storeup, req_dict)
                    
            except:
                pass
                
        else:
            msg.code = 500
            msg.msg = "File type error"
                
        return JsonResponse(msg)

def storeup_sendemail(request):
    if request.method in ["POST", "GET"]:
        req_dict = request.session.get("req_dict")

        code = random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 4)
        to = []
        to.append(req_dict['email'])

        send_mail('user registration', 'Your registration verification code is???'+''.join(code)+'???,Please do not leak the verification code to others, if not yourself do not operate.  ', 'yclw9@qq.com', to, fail_silently = False)

        cursor = connection.cursor()
        cursor.execute("insert into emailregistercode(email,role,code) values('"+req_dict['email']+"','user','"+''.join(code)+"')")

        msg = {
            "msg": "send successfully",
            "code": 0
        }

        return JsonResponse(msg)

def storeup_autoSort2(request):
    
    if request.method in ["POST", "GET"]:
        req_dict = request.session.get("req_dict")
        cursor = connection.cursor()
        leixing = set()
        try:
            cursor.execute("select inteltype from storeup where userid = %d"%(request.session.get("params").get("id"))+" and tablename = 'storeup' order by addtime desc")
            rows = cursor.fetchall()
            for row in rows:
                for item in row:
                    leixing.add(item)
        except:
            leixing = set()
        
        L = []
        cursor.execute("select * from storeup where $intelRecomColumn in ('%s"%("','").join(leixing)+"') union all select * from storeup where $intelRecomColumn not in('%s"%("','").join(leixing)+"')")
        desc = cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()] 
        for online_dict in data_dict:
            for key in online_dict:
                if 'datetime.datetime' in str(type(online_dict[key])):
                    online_dict[key] = online_dict[key].strftime(
                        "%Y-%m-%d %H:%M:%S")
                else:
                    pass
            L.append(online_dict)


        return JsonResponse({"code": 0, "msg": '',  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":5,"list": L[0:6]}})

def storeup_value(request, xColumnName, yColumnName, timeStatType):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "success", "data": {}}
        
        where = ' where 1 = 1 '
        sql = ''
        if timeStatType == 'day':
            sql = "SELECT DATE_FORMAT({0}, '%Y-%m-%d') {0}, sum({1}) total FROM storeup {2} GROUP BY DATE_FORMAT({0}, '%Y-%m-%d')".format(xColumnName, yColumnName, where, '%Y-%m-%d')

        if timeStatType == 'month':
            sql = "SELECT DATE_FORMAT({0}, '%Y-%m') {0}, sum({1}) total FROM storeup {2} GROUP BY DATE_FORMAT({0}, '%Y-%m')".format(xColumnName, yColumnName, where, '%Y-%m')

        if timeStatType == 'year':
            sql = "SELECT DATE_FORMAT({0}, '%Y') {0}, sum({1}) total FROM storeup {2} GROUP BY DATE_FORMAT({0}, '%Y')".format(xColumnName, yColumnName, where, '%Y')
        L = []
        cursor = connection.cursor()
        cursor.execute(sql)
        desc = cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()] 
        for online_dict in data_dict:
            for key in online_dict:
                if 'datetime.datetime' in str(type(online_dict[key])):
                    online_dict[key] = online_dict[key].strftime(
                        "%Y-%m-%d %H:%M:%S")
                else:
                    pass
            L.append(online_dict)
        msg['data'] = L

        return JsonResponse(msg)

def storeup_o_value(request, xColumnName, yColumnName):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "success", "data": {}}
        
        where = ' where 1 = 1 '
        
        sql = "SELECT {0}, sum({1}) AS total FROM storeup {2} GROUP BY {0}".format(xColumnName, yColumnName, where)
        L = []
        cursor = connection.cursor()
        cursor.execute(sql)
        desc = cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()] 
        for online_dict in data_dict:
            for key in online_dict:
                if 'datetime.datetime' in str(type(online_dict[key])):
                    online_dict[key] = online_dict[key].strftime(
                        "%Y-%m-%d %H:%M:%S")
                else:
                    pass
            L.append(online_dict)
        msg['data'] = L

        return JsonResponse(msg)

def storeup_alipay(request):
    if request.method in ["POST", "GET"]:
        alipay = AliPay(
            appid=settings.ALIPAY_APP_ID,
            app_notify_url=None,
            app_private_key_string=settings.APP_PRIVATE_KEY_STRING,
            alipay_public_key_string=settings.ALIPAY_PUBLIC_KEY_STRING,
            sign_type=settings.ALIPAY_SIGN_TYPE,
            debug=True,
            config=AliPayConfig(timeout=15)
        )
        
        req_dict = request.session.get("req_dict")

        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no=req_dict['tradeno'],
            total_amount=req_dict['totalamount'],
            subject=req_dict['subject'],
            return_url='http://localhost:8080/django4j60g/storeup/notify',
            #notify_url=''
        )
        pay_url = 'https://openapi.alipaydev.com/gateway.do?' + order_string
        pay_url = '<form name="punchout_form" method="post" action="{0}"><input type="hidden" name="biz_content" ><input type="submit" value="pay now" style="display: none"></form>'.format(pay_url)
        
        return JsonResponse({'code': 0, "data": pay_url})

def storeup_notify(request):
    if request.method in ["POST", "GET"]:
        req_dict = request.session.get("req_dict")
        out_trade_no = req_dict['out_trade_no']
        cursor = connection.cursor()
        
        return redirect('http://localhost:8080/django4j60g/admin/dist/index.html#/storeup')


