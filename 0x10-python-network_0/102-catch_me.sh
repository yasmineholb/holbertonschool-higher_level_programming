#!/bin/bash
# cause the server to respond with a message
curl 0.0.0.0:5000/catch_me -s -L -X PUT -d "user_id=98" -H "Origin: HolbertonSchool"
