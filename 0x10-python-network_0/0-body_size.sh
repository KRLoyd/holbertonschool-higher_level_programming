#!/bin/bash
# Bash script to display the size of the body of the passed URL
curl -sI "$1" | grep 'Content-Length' | cut -d " " -f2
