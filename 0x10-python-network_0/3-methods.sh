#!/usr/bin/bash
# print all server methods
curl -sI "$1" | grep -i Allow | cut -d ' ' -f2-
