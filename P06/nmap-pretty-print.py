# Name of script: nmap-pretty-print.py
"""
Purpose:
  Nmap script to pretty print result of port scan
  Ref: https://www.studytonight.com/network-programming-in-python/integrating-port-scanner-with-nmap

Run: 
  Nil

Args:
  Nil

Output:
  Prints the dict structure of a port scan
  File: nmap-pretty-print.txt (Redirect standard output write to file)
"""  

def pretty_dict_json(print_dict: dict):
  """
  Python has a built-in package called json , which can be used to work with JSON data. The json library can parse JSON from strings or files. 
  The library parses JSON into a Python dictionary or list. It can also convert Python dictionaries or lists into JSON strings.

  Convert dict to json format print it to show the dict structure
  Ref: https://www.geeksforgeeks.org/how-to-convert-python-dictionary-to-json/

  Args:
      print_dict (dict): result of port scan
  """  
  import json
  print('\n')
  print('*** print json format*****')
  print(json.dumps(print_dict, indent = 2))

def pretty_print(print_dict: dict):
  """
  The pprint module in Python is a utility module that you can use to print data structures in a readable, pretty way. It's a part of the 
  standard library that's especially useful for debugging code dealing with API requests, large JSON files, and data in general.
  
  Use the pprint library to show the dict structure

  Args:
      print_dict (dict): result of port scan
  """  
  import pprint
  print('\n')
  print('*** pretty print dict: results *****')
  pprint.pprint(print_dict)

# main starts here
import nmap

# initialize the port scanner
nmScan = nmap.PortScanner()
print(f'Type of nmScan : {type(nmScan)}')

# scan localhost for ports in range 21-443
IP = '127.0.0.1'                            # IP = 'scanme.nmap.org'
print(f'Target IP      : {IP}')

# By default, Nmap scans the most common 1,000 ports for each protocol. There are 65535 ports that can be used for service. In our example,
# we are scanning TCP ports 22-443.
results = nmScan.scan(IP, '21-443')
print(f'Type of results: {type(results)}')

# print using pretty print library
pretty_print(print_dict=results)

# convert dict to json and pretty print
pretty_dict_json(print_dict=results)