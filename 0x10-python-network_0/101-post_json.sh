#!/bin/bash
# send json

# Send a POST request with the file contents as the body and store the response in a variable
response=$(curl -s -X POST -d "@$2" -H "Content-Type: application/json" "$1")

# Display the body of the response
echo "$response"
