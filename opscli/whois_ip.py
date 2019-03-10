""" Whois IP lookup using requests library """
import requests
import sys
import os
import json
import pprint

def main():
    http_response = getWhois(sys.argv[1])
    json_dict = json.loads(http_response.text)
    pprint.pprint(json_dict)
    

def getWhois(ip_addr):
    url = "http://ip-api.com/json/" + ip_addr
    r = requests.get(url)
    return r

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Example Usage: {} 8.8.8.8".format(os.path.basename(__file__)))
        sys.exit()
    
    main()