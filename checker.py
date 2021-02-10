#!/usr/bin/python
# Author : Youssef ABYAA
# https://twitter.com/josef0x
# version : (beta)

print(''' _____                        _              _____ _               _             
|  __ \                      (_)            / ____| |             | |            
| |  | | ___  _ __ ___   __ _ _ _ __  ___  | |    | |__   ___  ___| | _____ _ __ 
| |  | |/ _ \| '_ ` _ \ / _` | | '_ \/ __| | |    | '_ \ / _ \/ __| |/ / _ \ '__|
| |__| | (_) | | | | | | (_| | | | | \__ \ | |____| | | |  __/ (__|   <  __/ |   
|_____/ \___/|_| |_| |_|\__,_|_|_| |_|___/  \_____|_| |_|\___|\___|_|\_\___|_|   
                                                                                ''')

import requests,sys
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

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

if (len(sys.argv) != 2):
  print("Usage: python3 check.py domains.txt")
  sys.exit()

else:

  f = open(sys.argv[1],'r')
  lines = f.readlines()
  for line in lines:
    try:
      if (('http://' or 'https://' ) in line.strip()):
        url = line.strip()
      else:
        url = 'http://'+line.strip()
      s = requests.Session()
      retry = Retry(connect=3, backoff_factor=0.5)
      
      s.mount('http://stackoverflow.com', HTTPAdapter(max_retries=5))
      r = s.get(url, timeout=5)
    except requests.ConnectionError as e:
      print(bcolors.FAIL + "[!] : Connection ERROR (Max retries exceeded) on : " +bcolors.ENDC+url+"\n")
      continue
    except requests.Timeout as e:
        print("[!] : Timeout Error")
        continue
    except requests.RequestException as e:
        print("[!] : General Error")
        continue
    
    except KeyboardInterrupt:
        exit()
    
    
    if (r.status_code == 200):
        print('\x1b[6;30;42m' + '[OK] : 200' + '\x1b[0m', ':' , line,end='')
    else:
        print(r.status_code ,' : ' , line,end='')
    
    if (('<script' in r.text) and (len(r.text) > 2)):
      print('> Might be interesting')
    
    print('\n')
    
