#This the very easy way to create a own ip scanner.. and some example of python script..
#jst copy & pase for it....

import socket
from datetime import datetime
net1 = raw_input('Enter the IP address')
net2 = net1.split('.')
a = '.'
net3 = net2[0] + a + net2[1] + a + net2[2] + a
stn1 = int(raw_input("enter the frist Number "))
edn1 = int(raw_input("enter the last Number "))
edn1 = edn1 + 1
td1 = datetime.now()
def scan(addr):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((addr,135))
    if result == 0 :
        return 1
    else :
        return 0
def run1():
    for ip in xrange(stn1,edn1):
        addr = net3+str(ip)
        if (scan(addr)):
            print addr, "this address is live"
run1()

td2 = datetime.now()
total = td2-td1
print "scanning complete in ", total
