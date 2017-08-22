#!/bin/bash
# Bash script that sends a GET request to URL passed and prints body
curl -s "$1" -X GET -H "X-HolbertonSchool-User-Id:98"
