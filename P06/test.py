# python interpreter
import nmap
nm = nmap.PortScanner()
nm.scan('127.0.0.1', '22-443') # ('scanme.nmap.org','22-443')
print(nm.csv())