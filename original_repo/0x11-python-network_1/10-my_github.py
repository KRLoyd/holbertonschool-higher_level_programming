#!/usr/bin/python3
"""
Pyhton script to take Github credentials and uses the Github API
to display id associated
"""
if __name__ == "__main__":
    # import necessary modules
    from sys import argv
    import requests
    from requests.auth import HTTPBasicAuth

    # Set variables to passed parameters
    user_name = argv[1]
    user_pass = argv[2]
    gh_url = 'https://api.github.com/user'

    # Do request
    req = requests.get(gh_url, auth=HTTPBasicAuth(user_name, user_pass))
    # Get JSON of request
    json_req = req.json()
    # Print the id found
    print(json_req.get('id'))
