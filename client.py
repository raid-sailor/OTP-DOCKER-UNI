import socket 

s = socket.socket()
port = 9898
host_ip = '127.0.0.1'

def connect(port, host_ip):

    s.connect((host_ip, port))
    print (s.recv(1024).decode())
    s.close()


while True: 

    connect(port,host_ip)
