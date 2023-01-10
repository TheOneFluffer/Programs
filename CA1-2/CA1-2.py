"""
Purpose:
    This file contains the main menu of the program
    Ref: https://www.studytonight.com/network-programming-in-python/integrating-port-scanner-with-nmap

Run: 
    Nil

Args:
    Nil

Output:
    Prints items such as host, protocol, port and state after a port scan
    File: nmap-pretty-print-IPs-options-items.txt (Redirect standard output write to file)
"""  

import generalMethods as gm
import mainframe as mf

def mainMenu():
    print("***PSEC Info Security Apps***")
    print("1. Scan Network")
    print("2. Upload/download file using FTP")
    print("3. Send custom packet")
    print("4. Credits")
    print("0. Exit")
    print("Enter your choice")
    choice = gm.validateChoice(">> ", 0, 4)
    return choice

def main():
    choice = ""

    while (choice != 0):
        choice = mainMenu()
        if choice != 0:
            if choice == 1:
                '''Perform scan'''
                mf.scanNetwork()
                pass
            elif choice == 2:
                '''Upload/download file using FTP'''
                pass
            elif choice == 3:
                '''Send custom packet'''
                pass
            elif choice == 4:
                '''Credits'''
                mf.Credits()
                pass
        elif choice == 0:
            break

main()