#!/usr/bin/python
# Author : Youssef ABYAA
# https://twitter.com/josef0x
# version : 1.01

import requests,sys
import concurrent.futures
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import argparse
from datetime import datetime
import logging
from tqdm import tqdm

def print_ascii_title():
	print('''
	\t██╗░░░██╗██████╗░██╗░░░░░  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
	\t██║░░░██║██╔══██╗██║░░░░░  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
	\t██║░░░██║██████╔╝██║░░░░░  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
	\t██║░░░██║██╔══██╗██║░░░░░  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
	\t╚██████╔╝██║░░██║███████╗  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
	\t░╚═════╝░╚═╝░░╚═╝╚══════╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
	''')

class colors:
    """
      defines colors (for display)  
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    GREEN = '\033[92m'
    OKGREEN = '\x1b[6;30;42m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def parse_arguments():
    '''
        parses the list of arguments 
    '''
    parser = argparse.ArgumentParser(
            description='As the name indicates HTTP response checker ' \
            'is self-descriptive. It checks the HTTP response of a list of '\
            'URLs stored in a file, prints each URL\'s response status' \
            'to the standard output.' \
            'If no output file is supplied, the results are still stored in' \
            'the directory output_files/')

    parser.add_argument(
            '-i',
            dest='input_file',
            help='name of the file containing the list of URLs to check.',
            required=True)


    parser.add_argument(
            '-o',
            dest='output_file',
            help='name of the file in which the results should be stored.')

    return parser.parse_args() 

def get_response(url, timeout=10):
    s = requests.Session()
    r = s.get(url, timeout=timeout)

    if r.status_code == 200:
        # print(f'{colors.OKGREEN} [OK] : 200 {colors.ENDC} : {url}')
        return f'[OK] : 200 {url}\n'

    # print(f'{colors.WARNING} {r.status_code} {colors.ENDC} : {url}')
    return f'{r.status_code} : {url}\n'

def main():
    '''
        main function
    '''
    args = parse_arguments()
    
    input_file = args.input_file
    output_file = args.output_file

    # results are stored even if the output file was not specified
    if not output_file:
        now = datetime.now()
        output_file = f'output_files/{now.hour}-{now.minute}-{now.second}' \
                      f'_{now.day}-{now.month}-{now.year}.txt'


    with open(input_file, 'r') as f:
        lines = f.readlines()

    out = open(output_file, 'w+')

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
			
        for line in lines:
        
            # Checking if the HTTP/HTTPS URI Scheme is present
            if 'http://' in line.strip() or 'https://' in line.strip():
                url = line.strip()
            else:
                # Add http:// if not given
                url = 'http://' + line.strip()
            
            futures.append(
                executor.submit(
                    get_response, url=url, timeout=3
                )
            )

        for future in tqdm(concurrent.futures.as_completed(futures)):
            try:
                future.result()

                # r = get_response(url, timeout=5)
                
                # display_response(url, r.status_code)

                # out.write('[' + str(r.status_code) + ']: ' + url + '\n')
                out.write(future.result())

            except requests.ConnectionError as e:
                print("\n", colors.FAIL + "[!] : Connection ERROR (Max retries exceeded) on : " + colors.ENDC + url)
                continue

            except requests.Timeout as e:
                print("[!] : Timeout Error")
                continue

            except requests.RequestException as e:
                print("[!] : General Error")
                continue

            except KeyboardInterrupt:
                out.close()
                print("\nOutput saved in : " + output_file + '\n')
                exit()


    #if (('<script' in r.text) and (len(r.text) > 2)):
    #  print(' >' + bcolors.UNDERLINE + 'Might be interesting\x1b[0m')

    print("\nOutput saved in : " + output_file + '\n')
    out.close()


if __name__ == '__main__':
	#print_ascii_title()
	main()
