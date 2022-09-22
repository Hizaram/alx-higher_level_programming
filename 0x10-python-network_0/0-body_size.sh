#!/usr/bin/bash
# Gets the size of the size of the body of the response after a request is sent to a URL
curl -sI "$1" | grep -oiE 'Content-Length: [0-9]+' | cut -d ' ' -f2
