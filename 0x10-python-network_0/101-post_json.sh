#!/bin/bash
# Send a POST request with the file contents as the body
curl -s "$1" -X POST -H "Content-Type: application/json" -d @"$2"
