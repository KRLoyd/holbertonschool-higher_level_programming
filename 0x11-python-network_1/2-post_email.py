#!/usr/bin/python3
"""
Python script that takes in a URL and email,
sends a POST request with email as parameter,
displays the body of response decoded in utf-8.
"""
if __name__ == "__main__":
    # Import the necessary modules
    from sys import argv
    import urllib.parse
    import urllib.request

    # Set variables per passed parameters
    url_value = argv[1]
    email_value = argv[2]

    # set the value of data to be sent
    value = {'email': email_value}
    # ulencode values
    data = urllib.parse.urlencode(value)
    # encode data to ascii for bytes
    data = data.encode('ascii')

    # POST to the URL
    req = urllib.request.Request(url_value, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')

    # Print body of response
    print(the_page)
