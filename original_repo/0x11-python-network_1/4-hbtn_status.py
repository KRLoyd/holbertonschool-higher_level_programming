#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
using requests module
"""
if __name__ == '__main__':
    # import necessary module
    import requests

    url = 'https://intranet.hbtn.io/status'

    # request the URL
    req = requests.get(url)

    # Set variables to wanted info
    content = req.text
    content_type = type(content)

    # Print in format
    print("Body response:")
    print("\t- type: {}\n\t- content: {}".format(content_type, content))
