# main starts here
import nmap
import pprint
import json

# initialize the port scanner
nmScan = nmap.PortScanner()
print(f'Type of nmScan : {type(nmScan)}')
# scan localhost for ports in range 21-443
IP = '127.0.0.1' # IP = 'scanme.nmap.org'
print(f'Target IP   : {IP}')
results = nmScan.scan(IP, '21-32')
print(f'Type of results: {type(results)}')
# print using pretty print library
pprint.pprint(results)
# convert dict to json and pretty print
result_json = json.dumps(results)
pprint.pprint(result_json)
