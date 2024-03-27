#!/bin/bash
# send req
# curl -X PUT -d "user_id=98" -H "Origin: School" 0.0.0.0:5000:5000/catch_me
curl -X PUT -d "user_id=98" -H "Origin: School" 0.0.0.0:5000/catch_me_3 -s
