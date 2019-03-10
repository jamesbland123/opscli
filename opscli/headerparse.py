""" Tool/Module to Parse request header """
import requests
import sys
import os

def main(): 
    r = requests.get(sys.argv[1])
    for k,v in r.headers.items():
        print("{}: {}".format(k, v))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Example Usage: {} https://www.wikipedia.com".format(os.path.basename(__file__)))
        sys.exit()
    main()