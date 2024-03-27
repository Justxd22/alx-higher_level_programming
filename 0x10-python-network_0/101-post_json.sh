#!/bin/bash
# Send a POST request with the file contents as the body
curl -s -X POST -d "@$2" -H "Content-Type: application/json" "$1"