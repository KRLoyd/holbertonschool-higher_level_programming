#!/usr/bin/python3
"""
Python script to take in a string and sends a search request
to the Star Wars API
"""
if __name__ == "__main__":
    # Import modules
    from sys import argv
    import requests

    # Set variables
    name_to_search = argv[1]
    sw_url = 'https://swapi.co/api/people/'

    # Set payload
    payload = {'search': name_to_search}

    # Do request
    req = requests.get(sw_url, params=payload)
    req_json = req.json().get('results')

    # Find size of the dictionary
    dict_len = len(req_json)
    print("Number of result: {}".format(dict_len))

    # Print the names in the dictionary
    for item in req_json:
        item_name = item.get('name')
        print(item_name)
