#!/usr/bin/python3
"""
Python script to take in a letter and send a POST request
to http://0.0.0.0:5000/search_user with a letter as parameter.
If no user found, displays "No result"
"""
if __name__ == "__main__":
    # Import modules
    from sys import argv
    import requests

    # Check passed parameter
    if len(argv) < 2 or not argv[1].isalpha():
        print("No result")
    else:
        # Set value to the q variable and passed param
        value = {'q': argv[1]}
        # Make the request
        req = requests.post('http://0.0.0.0:5000/search_user', data=value)
        # Get JSON of request
        try:
            id_val = req.json().get('id')
            name_val = req.json().get('name')
            print('[{}] {}'.format(id_val, name_val))
        except:
            print("Not a valid JSON")
