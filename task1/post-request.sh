#!/usr/bin/env bash


host="https://jsonplaceholder.typicode.com/posts"
outfile="jsonplaceholder_response.json"

#curl -X POST "https://jsonplaceholder.typicode.com/posts/1/comments" -o jsonplaceholder_response.json

# specifying headers
# curl -H "X-First-Name: Joe"
curl -Ss -XPOST "$host" -o "$outfile" # -d '{"data":"foo"}'

#curl -X POST "$host" -o jsonplaceholder_response.json


