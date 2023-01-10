# run python portScanThread.py localhost 22 443
# https://stackoverflow.com/questions/26174743/making-a-fast-port-scanner
import threading
import socket
import sys
# target = 'localhost'
target = sys.argv[1]            # need import sys; host is a string
portStart = int(sys.argv[2])    # port must be numeric
portEnd   = int(sys.argv[3])    # port must be numeric
def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)# 
    try:
        con = s.connect((target,port))
        print('Port :',port,"is open.")
        con.close()
    except: 
        print('Port :',port,"is closed.")
for x in range(portStart,portEnd):
    # print(x)
    t = threading.Thread(target=portscan,kwargs={'port':x})    
    t.start()