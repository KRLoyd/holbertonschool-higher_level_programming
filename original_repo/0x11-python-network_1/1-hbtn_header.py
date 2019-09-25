#!/usr/bin/python3
"""
Python script to take a URL as an argument,
requests the URL, and displays the value of variable X-Request-Id
"""
if __name__ == "__main__":
    from sys import argv
    import urllib.request

    url = argv[1]

    with urllib.request.urlopen(url) as response:
        requested_info = response.info().get('X-Request-Id')

    print(requested_info)
