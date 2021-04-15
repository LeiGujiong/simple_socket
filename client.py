#client

import socket

HOST = '172.22.229.120' #设置本地服务器号
PORT = 28888 #设置端口号

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #选择IPv4地址以及TCP协议
sock.connect((HOST, PORT)) #连接端口

print("try to connect distance server")
sock.send(b'request')
re_mes = sock.recv(1024).decode()
print(re_mes)

if re_mes == "welcome to server!":
    while True:
        print("用户端请输入：")
        a = input()
        sock.send((a).encode("utf-8"))
        print("等待服务器回复，请勿输入：")
        re_mes = sock.recv(1024).decode()
        if re_mes == "close":
            break
        print(re_mes)
sock.close()
print("连接关闭")
