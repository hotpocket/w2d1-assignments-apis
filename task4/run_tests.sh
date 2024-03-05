#!/usr/bin/env bash

# start the server
python3 ./server.py &
serverPid="$!"
# sleep for 0.1s , give the server a chance to start
read -t 0.1

# run the client
python3 ./client.py

# kill the server
kill $serverPid
