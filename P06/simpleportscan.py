# https://www.geeksforgeeks.org/simple-port-scanner-using-sockets-in-python/
import socket
import time
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
target = '127.0.0.1'
# get the ip address of the target
target_ip = socket.gethostbyname(target)
print('Starting scan on host:', target_ip)
# function for scanning ports
def port_scan(port):
  try:
    s.connect((target_ip, port))
    return True
  except:
    return False
start = time.time()
for port in range(442,450):
  if port_scan(port):
    print(f'port {port} is open')
  else:
    print(f'port {port} is closed')
end = time.time()
print(f'Time taken {end-start:.2f} seconds')
