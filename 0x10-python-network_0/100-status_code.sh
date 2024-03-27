#!/bin/bash
# print req code status
response_headers=$(curl -sI "$1")
status_code=$(echo "$response_headers" | head -n 1 | cut -d ' ' -f 2)
echo "$status_code"

