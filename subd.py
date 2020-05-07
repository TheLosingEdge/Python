import requests 
import sys
import socket

sub_list = open("subdomains-1000.txt").read() 
subs = sub_list.splitlines()

for sub in subs:
    url_to_check = f"http://{sub}.{sys.argv[1]}" 

    try:
        requests.get(url_to_check)
    
    except requests.ConnectionError: 
        pass
    
    else:
        gethostby_ = socket.gethostbyname(sys.argv[1])
        print("Valid domain: ",url_to_check,gethostby_)