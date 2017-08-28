#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
Its body is displayed.
"""
if __name__ == "__main__":
    import urllib.request

    url = 'https://intranet.hbtn.io/status'

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        page_content = response.read()

    content_type = type(page_content)

    utf8_content = page_content.decode('utf-8')

    print("Body response:")
    print("\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(
        content_type, page_content, utf8_content))
