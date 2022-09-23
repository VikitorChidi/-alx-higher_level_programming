#!/bin/bash
# Script that makes a request to causes an specific response
curl -sL 0.0.0.0:5000/catch_me -X PUT "user_id=98" -H "Origin: School"
