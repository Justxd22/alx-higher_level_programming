#!/bin/bash
# print req size
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
