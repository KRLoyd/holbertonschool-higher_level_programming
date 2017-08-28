#!/usr/bin/python3
"""
Python script to take in a URL and email address.
Sends a POST request to the passed URL with email as parameter.
Displays the body of the response.
"""
if __name__ == '__main__':
    # import necessary module
    import sys
    import requests

    # Set variables to passed parameter
    url_val = sys.argv[1]
    email_val = sys.argv[2]

    # Set payload to the dict with email
    payload = {'email': email_val}

    # request the head of  URL
    req = requests.post(url_val, data=payload)

    # Print the the response
    print(req.text)
