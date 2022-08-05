import time
import hashlib
import requests

f=open("result.txt","a")

#日志功能
def log(f,str_log):
    f.write(str_log)

#获取客户端列表
def getclientlist(host):
    now = int(time.time())
    m = hashlib.md5()
    m.update(str(int(now)).encode("utf8"))
    auth_key = m.hexdigest()
    data={
        'search':'',
        'order':'asc',
        'offset':'0',
        'limit':'10',
        'auth_key':auth_key,
        'timestamp':str(now)
    }
    if "http" not in host:
        url="http://"+str(host)+"/client/list"
    else: url=str(host)+"/client/list"
    r=requests.post(url,data,timeout=3)
    if r.status_code is 200 and "/html" not in r.text:
        return r.text
    else: return "flase"

# 添加客户端
def addclent(host):
    now = int(time.time())
    m = hashlib.md5()
    m.update(str(int(now)).encode("utf8"))
    auth_key = m.hexdigest()
    data={
        'remark':'',
        'u':'',
        'p':'',
        'vkey':'',
        'config_conn_allow':'1',
        'compress':'0',
        'crypt':'0',
        'auth_key':auth_key,
        'timestamp':str(now)
    }
    if "http" not in host:
        url="http://"+str(host)+"/client/add"
    else: url=str(host)+"/client/add"
    r=requests.post(url,data,timeout=3)
    if r.status_code is 200 and "/html" not in r.text:
        return r.text
    else: return "flase"

#删除客户端
def delclent(host,id):
    now = int(time.time())
    m = hashlib.md5()
    m.update(str(int(now)).encode("utf8"))
    auth_key = m.hexdigest()
    data={
        'id':id,
        'auth_key':auth_key,
        'timestamp':str(now)
    }
    if "http" not in host:
        url="http://"+str(host)+"/client/del"
    else: url=str(host)+"/client/del"
    r=requests.post(url,data,timeout=3)
    if r.status_code is 200 and "/html" not in r.text:
        return r.text
    else: return "flase"

#修改状态 0:停止 1:开始
def changeclent(host,status):
    now = int(time.time())
    m = hashlib.md5()
    m.update(str(int(now)).encode("utf8"))
    auth_key = m.hexdigest()
    data={
        'id':id,
        'status':status,
        'auth_key':auth_key,
        'timestamp':str(now)
    }
    if "http" not in host:
        url="http://"+str(host)+"/client/changestatus"
    else: url=str(host)+"/client/changestatus"
    r=requests.post(url,data,timeout=3)
    if r.status_code is 200 and "/html" not in r.text:
        return r.text
    else: return "flase"
