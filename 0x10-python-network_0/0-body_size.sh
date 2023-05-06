#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI "$I" | awk '/content-length/ { print $2 }'
