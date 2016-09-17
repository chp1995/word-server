# -*- coding: utf-8 -*-
import time, socket, threading

def link(sock, addr):
    #print 'Accept new connection from %s:%s...' % addr
    sock.send('Hello!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        #如果客户端发送了exit字符串，就直接关闭连接
        if data == 'exit' or not data:
            break
        data.reverse()
        sock.send(data)
    sock.close()
    print 'Connection from %s:%s closed.' % addr


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('127.0.0.1', 3333))
s.listen(5)
print 'Waiting for connection...'
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=link, args=(sock, addr))
    t.start()
