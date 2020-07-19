import requests
import xmltodict
import argparse ,sys
import bcolors

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
    if(sys.argv[1] != 'u'):
        try:
            input_url = sys.argv[2]
            input_header = requests.get(input_url)
            input_status_code = input_header.status_code
            parse_text = xmltodict.parse(input_header.text)

            try:
                error_parse_text = parse_text['Error']['Code']
                if(error_parse_text == 'NoSuchBucket'):
                    print("Bucket available for sub domain takeover")
                elif(error_parse_text == 'Access Denied'):
                    print('Bucket not available for sub domain takeover')
            except:
                if(input_status_code == 200):
                    print('Bucket not available for sub domain takeover')
        except:
            print('Please enter python bucket-takeover.py -u < valid URL>')
            print("Give Domain with http:// or https://")

    elif (sys.argv[1] != '-u'):
        print('Please enter -u <valid bucket URL>')
else:
    banner()
    print(bcolors.ERR + 'Please select at-least 1 option from -u , with a valid bucket name')

