#!/bin/bash
# print req code status
curl -s -o /dev/null -w "%{http_code}" "$1"
