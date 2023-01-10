# main starts here
import nmap
import pprint

# initialize the port scanner
nmScan = nmap.PortScanner()
print(f'Type of nmScan : {type(nmScan)}')
# scan multiple hosts/specify options
IP = 'localhost scanme.nmap.org'
print(f'Target IP   : {IP}')
options = '-p 22-32 -sTU -T5'   # scanning TCP and UDP ports
results = nmScan.scan(hosts=IP, arguments=options)
print(f'Type of results: {type(results)}')
# convert dict to json and pretty print
pprint.pprint(results)
