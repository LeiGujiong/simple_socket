
#server
import socket

HOST = '172.22.229.120' #设置本地服务器号
# 在树莓派中测试的时候使用的服务号为172.22.229.120
HOST = '172.22.229.120'
PORT = 28888 #设置端口好

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #选择IPv4地址以及TCP协议
sock.bind((HOST, PORT)) #绑定端口
sock.listen(5) #监听这个端口，可连接最多5个设备

while True:
    connection, address = sock.accept() #等待客户端的连接请求
    # build_connection就是客户端连过来而在服务器端为其生成的一个连接实例
    build_connection = connection.recv(1024) #接受数据实例化 什么意思？？
    
    if build_connection == b"request":
        print("connection is ok!")
        connection.send(b'welcome to server!')
        connection_flag = True #连接标志位
    else:
        connection_flag = False
        break

    #若连接成功的话，开始进行接收和发送的半双工工作
    while connection_flag == True:
        print("等待用户端回复，请勿输入：")
        a = connection.recv(1024) 
        if a == b"close":
            #connection.send(1024)
            print("用户端取消连接")
            break
        if a != b"request" and a:
            print("客户端输入为：")
            print((a).decode())
            print("服务器请输入：")
            se = input()
            connection.send((se).encode("utf-8"))
            if se == "close":
                break
            #print("") 

    break
connection.close()
print("连接关闭")
