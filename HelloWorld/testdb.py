# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from TestModel.models import Test
from TestModel.models import UserInfo
from TestModel.models import Communicate
from TestModel.models import Delegate
from TestModel.models import Notif
from TestModel.models import Location

import json
import time
import datetime

def zanPlus(request):
    request.encoding='utf-8'
    username='username'
    time='time'
    if 'username' in request.GET:
        username=request.GET['username']
    if 'time' in request.GET:
        time=request.GET['time']
    commu=Communicate.objects.get(userName=username,ctime=time)
    commu.zan=str(eval(commu.zan)+1)
    commu.save()
    return HttpResponse("OK")
    


def zanMinus(request):
    request.encoding='utf-8'
    username='username'
    time='time'
    if 'username' in request.GET:
        username=request.GET['username']
    if 'time' in request.GET:
        time=request.GET['time']
    commu=Communicate.objects.get(userName=username,ctime=time)
    commu.zan=str(eval(commu.zan)-1)
    commu.save()
    return HttpResponse("OK")
def del_delegate(request):
    request.encoding='utf-8'
    username='username'
    time='time'
    if 'username' in request.GET:
        username=request.GET['username']
    if 'time' in request.GET:
        time=request.GET['time']
    # 删除id=1的数据
    delegate=Delegate.objects.filter(userName=request.GET['username'],dtime=request.GET['time']).delete()
    # test1 = Test.objects.get(id=1)
    # delegate.delete()
    return HttpResponse("OK")
    # 另外一种方式
    # Test.objects.filter(id=1).delete()
    
    # 删除所有数据
    # Test.objects.all().delete()
    
    return HttpResponse("<p>删除成功</p>")
def new_delegate(request):
    request.encoding='utf-8'
    username='username'
    time='time'
    lng='0.0'
    lat='0.0'
    Content='content'
    if 'username' in request.GET:
        username=request.GET['username']
    if 'time' in request.GET:
        time=request.GET['time']
    if 'lat' in request.GET:
        lat=request.GET['lat']
    if 'lng' in request.GET:
        lng=request.GET['lng']
    if 'content' in request.GET:
        Content=request.GET['content']
    delegate=Delegate(userName=username,dtime=time,locationLat=lat,locationLng=lng,remark=Content)
    delegate.save()
    return HttpResponse("OK")
    

def pub_communicate(request):
    request.encoding='utf-8'
    username='username'
    time='time'
    imgUrl='imageUrl'
    lng='0.0'
    lat='0.0'
    Content='content'
    if 'username' in request.GET:
        username=request.GET['username']
    if 'time' in request.GET:
        time=request.GET['time']
    if 'lat' in request.GET:
        lat=request.GET['lat']
    if 'lng' in request.GET:
        lng=request.GET['lng']
    if 'content' in request.GET:
        Content=request.GET['content']
    commu=Communicate(userName=username,ctime=time,Location=lat,imageUrl=imgUrl,content=Content,zan='0')
    commu.save()
    return HttpResponse("OK")

def load_delegate(request):
    request.encoding='utf-8'
    delegate=[]
    if 'username' in request.GET:
        delegate=Delegate.objects.filter(userName=request.GET['username']).order_by('-dtime')
    response={0:{}}
    i=0
    for item in delegate:
        response[i]={'userName':item.userName,'time':item.dtime,'lng':item.locationLng,'lat':item.locationLat,'content':item.remark}
        i=i+1
    return HttpResponse(json.dumps(response))

def load_notif(request):
    request.encoding='utf-8'
    delegate=[]
    if 'location' in request.GET:
        delegate=Delegate.objects.filter(location=request.GET['location']).order_by('-dtime')
    response={0:{}}
    i=0
    for item in delegate:
        response[i]={'userName':item.userName,'time':item.dtime,'lng':item.locationLng,'lat':item.locationLat,'content':item.remark}
        i=i+1
    return HttpResponse(json.dumps(response))

def join(request):
    request.encoding='utf-8'
    location=[]
    if 'location' in request.GET:
        location=Location.objects.filter(name=request.GET['location'])
    for item in location:
        item.people=str(max(eval(item.people)+1,0))
        item.save()
    return HttpResponse('OK')

def leave(request):
    request.encoding='utf-8'
    location=[]
    if 'location' in request.GET:
        location=Location.objects.filter(name=request.GET['location'])
    for item in location:
        item.people=str(max(eval(item.people)-1,0))
        item.save()
    return HttpResponse('OK')

def peoplenum(request):
    request.encoding='utf-8'
    location=[]
    if 'location' in request.GET:
        location=Location.objects.filter(name=request.GET['location'])
    result=''
    if len(location)==0:
        return HttpResponse('0')
    for item in location:
        result=item.people
    return HttpResponse(result)

def msg_after(request):
    request.encoding='utf-8'
    delegate=[]
    req_time=''
    if 'location' in request.GET:
        delegate=Delegate.objects.filter(locationLng=request.GET['location'])
    username=''
    
    if 'username' in request.GET:
        username=request.GET['username']
    result=''
    num=0
    if len(delegate)==0:
        return HttpResponse('0')
    for item in delegate:
        a=time.mktime(time.localtime())
        b=time.mktime(time.strptime(item.dtime,"%Y-%m-%d %H:%M:%S"))
        if a-b<6 and a-b>-6:
            num=num+1
    if(num>0):
        result='YES'
    else:
        result='NO'
    return HttpResponse(result)


def load_communicate(request):
    request.encoding='utf-8'
    commu=[]
    if 'load' in request.GET:
        commu=Communicate.objects.all().order_by('-ctime')
    response={0:{}}
    i=0
    for item in commu:
        response[i]={'userName':item.userName,'time':item.ctime,'lng':item.Location,'lat':item.Location,'content':item.content,'zan':item.zan}
        i=i+1
    return HttpResponse(json.dumps(response))
def check_login(request):
    request.encoding='utf-8'
    username='username'
    if 'username' in request.GET:
        username=request.GET['username']
    true_password=UserInfo.objects.filter(userName=username)
    true_password=true_password.values("pasword")
    return HttpResponse(true_password)
    

def register(request):
    request.encoding='utf-8'
    username='username'
    password='123456'
    realname='realname'
    stuid='stuid'
    if 'username' in request.GET:
        username=request.GET['username']
    if 'password' in request.GET:
        password=request.GET['password']
    if 'realname' in request.GET:
        realname=request.GET['realname']
    if 'stuid' in request.GET:
        stuid=request.GET['stuid']
    
    this_user=UserInfo.objects.filter(userName=username)
    if len(this_user)>0:
        return HttpResponse("NO")
    new_user=UserInfo(userName=username,pasword=password,iden=stuid,realName=realname)
    new_user.save()
    return HttpResponse("OK")
# 数据库操作
def testdb(request):
    # 初始化
    response = ""
    response1 = ""

    
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()
        
    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id=1) 
    
    # 获取单个对象
    response3 = Test.objects.get(id=1) 
    
    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    Test.objects.order_by('name')[0:2]
    
    #数据排序
    Test.objects.order_by("id")
    
    # 上面的方法可以连锁使用
    Test.objects.filter(name="runoob").order_by("id")
    
    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")


# 数据库操作
def testalt(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = Test.objects.get(id=1)
    test1.name = 'Google'
    test1.save()
    
    # 另外一种方式
    #Test.objects.filter(id=1).update(name='Google')
    
    # 修改所有的列
    # Test.objects.all().update(name='Google')
    
    return HttpResponse("<p>修改成功</p>")

# 数据库操作
def testdel(request):
    # 删除id=1的数据
    test1 = Test.objects.get(id=1)
    test1.delete()
    
    # 另外一种方式
    # Test.objects.filter(id=1).delete()
    
    # 删除所有数据
    # Test.objects.all().delete()
    
    return HttpResponse("<p>删除成功</p>")