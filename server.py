import socket 
import random
import string

# set the port and the socket name 
s = socket.socket()
port = 9898

# bind the port together 
s.bind(('', port))

print('Socket binded to %s' %(port))

s.listen(5)

# this will print out a random string of of ascii_letters with a range of 12. This will be the actual OTP
result_str = ''.join(random.choice(string.ascii_letters) for i in range(12))

# print the actual OTP 
resultz = "Your One Time Password is: " + result_str

# A while loop until the process is complete 
while True:

    c, addr = s.accept()
    c.send(resultz.encode())

    c.close()

    break