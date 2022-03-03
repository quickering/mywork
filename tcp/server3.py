import socket
import re
import threading,time
server = socket.socket()             #初始化
server.bind(('127.0.0.1',9000))      #绑定ip和端口
 
server.listen(5)                     #监听，设置最大数量是5
print("开始等待接受客户端数据----")
def tcplink(conn,addr):
    while True:
              #获取客户端地址
        print(conn,addr)
        print("客户端来数据了")
        while True:
            data = conn.recv(1024)       #接收数据
            print("接受的数据：",data)
            d=data.decode('utf-8')
            print(d)
            # print(d[0],d[1],d[2])

            if not d or d=='exit':
                print("client has lost")
                break
            # if eval(d) is True:
            #     conn.send(str(eval(d)).encode('utf-8'))
            
            elif d=='hello':
                    conn.send((d+',this is server %s:%s.' % addr).encode('utf-8'))    #返回数据
            elif ' ' in d:
                    m=d.split()[1]
                    n=d.split()[0]
                    print(m,n)
                    a=re.findall(m,n)
                    print(a)
                    conn.send(str(a).encode('utf-8'))
            elif '+'in d:
                    try:
                        # print(i)
                        a=eval(d)
                        conn.send(str(a).encode('utf-8'))
                    except Exception as e:
                        print('wrong{}'.format(type(e)))
            elif '-'in d:
                try:
                    # print(i)
                    a=eval(d)
                    conn.send(str(a).encode('utf-8'))
                except Exception as e:
                    print('wrong{}'.format(type(e)))
            elif '*'in d:
                try:
                    # print(i)
                    a=eval(d)
                    conn.send(str(a).encode('utf-8'))
                except Exception as e:
                    print('wrong{}'.format(type(e)))
            elif '/'in d:
                try:
                    # print(i)
                    a=eval(d)
                    conn.send(str(a).encode('utf-8'))
                except Exception as e:
                    print('wrong{}'.format(type(e)))
            else:
                conn.send(str(d).encode('utf-8'))

while True:
    conn,addr=server.accept()
    t=threading.Thread(target=tcplink,args=(conn,addr))
    t.start()