#!/bin/bash
# Bash script that sends a GET request to a URL and displays the body of the response
curl -H 'X-School-User-Id:98' -sLX GET "$1"
