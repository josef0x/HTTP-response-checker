#!/usr/bin/python
# Author : Youssef ABYAA
# https://twitter.com/josef0x
# version : 0.02

import requests,sys
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

print('''
\t██╗░░░██╗██████╗░██╗░░░░░  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
\t██║░░░██║██╔══██╗██║░░░░░  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
\t██║░░░██║██████╔╝██║░░░░░  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
\t██║░░░██║██╔══██╗██║░░░░░  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
\t╚██████╔╝██║░░██║███████╗  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
\t░╚═════╝░╚═╝░░╚═╝╚══════╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
''')

# COLORS #
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Checking the number of arguments
if (len(sys.argv) != 2):
  print("\nUsage: python3 check.py URLs.txt\n")
  sys.exit()

else:
  f = open(sys.argv[1],'r') # Opening the text file
  lines = f.readlines()
  f.close()

  filename = 'output_files/' + sys.argv[1].replace('../','') + '_output.txt'
  out = open(filename, 'w+')

  # At this point lines is a list containing the URLs inside the text file
  for line in lines:
    try:
      # Checking if the HTTP/HTTPS URI Scheme is present
      if 'http://' in line.strip() or 'https://' in line.strip():
        url = line.strip()
      else:
        # In case it is not specified we add it
        url = 'http://' + line.strip()
      
      s = requests.Session()
#      retry = Retry(connect=3, backoff_factor=0.5)
      
#      s.mount('http://github.com', HTTPAdapter(max_retries=5))
      r = s.get(url, timeout=5)
  
      out.write(url + ':' + str(r.status_code) + '\n')

    except requests.ConnectionError as e:
      print("\n", bcolors.FAIL + "[!] : Connection ERROR (Max retries exceeded) on : " + bcolors.ENDC + url)
      continue
    except requests.Timeout as e:
        print("[!] : Timeout Error")
        continue
    except requests.RequestException as e:
        print("[!] : General Error")
        continue
    
    except KeyboardInterrupt:
      out.close()
      print("\nOutput saved in : " + filename + '\n')
      exit()
    
    # Printing the results
    if (r.status_code == 200):
        print("\n", '\x1b[6;30;42m' + '[OK] : 200', bcolors.ENDC, ':' , url)
    else:
        print('\n', bcolors.WARNING, r.status_code , bcolors.ENDC, ' : ' , url)

    if (('<script' in r.text) and (len(r.text) > 2)):
      print(' >' + bcolors.UNDERLINE + 'Might be interesting\x1b[0m')
  
  print("\nOutput saved in : " + filename + '\n')
  out.close()
