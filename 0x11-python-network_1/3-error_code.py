#!/usr/bin/python3
"""
Python script to take in a URL, sends a request to the URL,
and displays the body of the response decpded in utf-8.
Errors are handled and printed.
"""
if __name__ == "__main__":
    # Import necessary modules
    import sys
    import urllib.request
    import urllib.error

    # Set variables per passed parameters
    url = sys.argv[1]

    # Make request
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            result = response.read()
    except urllib.error.HTTPError as e:
        print("Error code: ", e.code)
    else:
        decoded_content = result.decode('utf-8')
        print(decoded_content)
