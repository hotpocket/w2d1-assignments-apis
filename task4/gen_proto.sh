#!/usr/bin/env bash

# enables aliases ... but i decided to go w/ a function instead
#shopt -s expand_aliases

compile() {
  echo "$1" | grep -E '^.*?.proto$' > /dev/null
  if [ "$?" != "0" ];then
    echo "ERROR: $1 is not a .proto file"
    return -1
  fi
  fname=`echo "$1" | sed 's/.proto$//'`
  echo
  echo "Generating:"
  echo "  ${fname}_pb2.py"
  echo "  ${fname}_pb2.pyi"
  echo "  ${fname}_pb2_grpc.pyi"
  python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. "$1"
}


compile echo.proto
