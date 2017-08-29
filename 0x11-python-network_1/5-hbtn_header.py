#!/usr/bin/python3
"""
Python script that fetches URL passed to script.
Displays the value of variable X-Request-Id.
Uses requests module.
"""
if __name__ == '__main__':
    # import necessary module
    import sys
    import requests

    # Set variables to passed parameter
    url_val = sys.argv[1]

    # request the head of  URL
    req = requests.get(url_val)
    # Get the variable X-Request-Id from header
    try:
        req_var = req.headers['x-request-id']
        # Print it
        print(req_var)
    except:
        print("None")
