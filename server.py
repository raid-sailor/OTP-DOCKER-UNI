import socket 
import random
import string
import os 

# set the port and the socket name 
s = socket.socket()
port = 9898

# bind the port together 
s.bind(('', port))



s.listen(5)

# this will print out a random string of of ascii_letters with a range of 12. This will be the actual OTP
result_str = ''.join(random.choice(string.ascii_letters) for i in range(12))

# print the actual OTP 
resultz = "Your One Time Password is: " + result_str

# A while loop 

def login():

    # a loop which will give a total of 3 attempts to get the password right  
    for x in range(3):

        # input for the username and password 
        print("Download a client script 👉🏻 https://raw.githubusercontent.com/raid-sailor/OTP-DOCKER-UNI/main/client.py")
        usr = input("\nEnter username: ")
        psw = input("Enter password: ")
        
        # this is hardcoded for now but future versions will include a keychain function and other encrypted authz. 
        if usr == "dan" and psw == "dan":
            
           
            c, addr = s.accept()
            c.send(resultz.encode())
            os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
            print("Sent OTP to client: " + result_str + "\n")
            c.close()

            break
        

        else:

            print("Access Denied!")
            print("Username or password incorrect, please try again.\n")
    else:

        print("Closing down.")

login()