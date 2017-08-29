#!/usr/bin/python3
"""
Python script to take a URL, send a request to it,
and display the body of the response.
If the status of the response is >= 400, the error code is displayed.
"""
if __name__ == "__main__":
    # Import necessary modules
    from sys import argv
    import requests

    # Set url_val to passed URL
    url_val = argv[1]

    # Send request to URL
    req = requests.get(url_val)

    # get the status_code of request
    status = req.status_code

    # Check if status is >= 400
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(req.text)
