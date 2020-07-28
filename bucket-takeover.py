import requests
import xmltodict
import argparse, sys
import bcolors
import os
import re


def banner():
    print("""

        ██╗░░░██╗███╗░░██╗░█████╗░██╗░░░░░░█████╗░██╗███╗░░░███╗░░░░░░░██████╗██████╗░░░░░░░███████╗██╗███╗░░██╗██████╗░███████╗██████╗░
        ██║░░░██║████╗░██║██╔══██╗██║░░░░░██╔══██╗██║████╗░████║░░░░░░██╔════╝╚════██╗░░░░░░██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
        ██║░░░██║██╔██╗██║██║░░╚═╝██║░░░░░███████║██║██╔████╔██║█████╗╚█████╗░░█████╔╝█████╗█████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
        ██║░░░██║██║╚████║██║░░██╗██║░░░░░██╔══██║██║██║╚██╔╝██║╚════╝░╚═══██╗░╚═══██╗╚════╝██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
        ╚██████╔╝██║░╚███║╚█████╔╝███████╗██║░░██║██║██║░╚═╝░██║░░░░░░██████╔╝██████╔╝░░░░░░██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
        ░╚═════╝░╚═╝░░╚══╝░╚════╝░╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝░░░░░░╚═════╝░╚═════╝░░░░░░░╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
                                                                                                                             Code by NG          
              """)
if len(sys.argv) > 1:
    banner()
    if (sys.argv[1] != 'u'):
        try:
            bucket = sys.argv[2]
            input_url = 'https://' + bucket + '.s3.amazonaws.com'
            input_location = sys.argv[2]
            if(os.path.exists(input_location)==True):
                file = open(input_location, "r")
                line = file.readlines()
                for text in line:
                    lines = 'https://' + text.rstrip() + '.s3.amazonaws.com'
                    try:
                        input_header = requests.get(lines)
                        input_status_code = input_header.status_code
                        parse_text = xmltodict.parse(input_header.text)
                        error_parse_text = parse_text['Error']['Code']
                        if (error_parse_text == 'NoSuchBucket'):
                                print( bcolors.OKMSG + text + "Bucket available for sub domain takeover")
                        elif (error_parse_text == 'AccessDenied'):
                                print(bcolors.OKMSG + text + 'Bucket not available for sub domain takeover access denied')
                    except:
                         if (input_status_code == 200):
                                print(bcolors.OKMSG + text + 'Bucket not available for sub domain takeover code 200')

            elif (os.path.exists(input_location) == False):
                input_header = requests.get(input_url)
                input_status_code = input_header.status_code
                parse_text = xmltodict.parse(input_header.text)
                try:
                    error_parse_text = parse_text['Error']['Code']
                    if (error_parse_text == 'NoSuchBucket'):
                        print(bcolors.OKMSG + bucket + " Bucket available for sub domain takeover")
                    elif (error_parse_text == 'AccessDenied'):
                        print(bcolors.OKMSG + bucket + ' Bucket not available for sub domain takeover')
                except:
                    if (input_status_code == 200):
                        print(bcolors.OKMSG + bucket + 'Bucket not available for sub domain takeover')

        except:
            print('Please enter python bucket-takeover.py -u < valid URL>')
            print("Give Domain with http:// or https://")

    elif (sys.argv[1] != '-u'):
        print('Please enter -u <valid bucket URL>')
else:
    banner()
    print(bcolors.ERR + 'Please select at-least 1 option from -u , with a valid bucket name')

