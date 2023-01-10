import nmap
nm = nmap.PortScanner()
print(nm.scan('127.0.0.1', '22-32')) # ('scanme.nmap.org','22-443')

# nm.scan('127.0.0.1', '22-32') # ('scanme.nmap.org','22-443')
# print(nm.csv())
