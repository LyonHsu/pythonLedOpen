# !/usr/bin/python
# coding:utf-8
import socket;
import os
def getLocalIp():
    hostname = socket.gethostname();
    ip=socket.gethostbyname(socket.gethostname());
    print("hostname=%d",hostname);
    print("ip=%d",ip);
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    localIp=s.getsockname()[0]
    print(s.getsockname()[0])
    s.close()
    return localIp
ip = getLocalIp()
ip=ip.replace("."," 點 ")
cmd = 'espeak -s 100 -vzh+f5 " {}" '.format(ip) 
os.system('espeak -s 150 -v+f5 "  i p is "')
os.system(cmd)
