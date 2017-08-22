#!/bin/bash
# Bash script to display all HTTP methods accepted by the passed server
curl -sI "$1" | grep "Allow" | cut -d ":" -f2 | cut -d " " --fields=2-
