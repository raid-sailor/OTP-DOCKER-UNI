import socket 
import os

s = socket.socket()
port = 9898
host_ip = '127.0.0.1'

def connect(port, host_ip):

    s.connect((host_ip, port))
    print (s.recv(1024).decode())
    s.close()

def clear():
    
    # this will clear the screen based on os. 
    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')

def login():

    # a loop which will give a total of 3 attempts to get the password right  
    for x in range(3):

        # input for the username and password 

        usr = input("Enter username: ")
        psw = input("Enter password: ")
        
        # this is hardcoded for now but future versions will include a keychain function and other encrypted authz. 
        if usr == "dan" and psw == "dan":
            
            clear()
            connect(port,host_ip)
            break
        

        else:

            print("Access Denied!")
            print("Username or password incorrect, please try again.\n")
    else:

        print("Closing down.")

login()