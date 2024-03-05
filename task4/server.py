from concurrent import futures
import time

import grpc
import echo_pb2
import echo_pb2_grpc

import signal
import sys

class Echo(echo_pb2_grpc.EchoServicer):
    def EchoMessage(self, request, context):
      print(f'Server: received "{request.message}" from client.')
      return echo_pb2.EchoResponse(message=request.message)

def start_server():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    echo_pb2_grpc.add_EchoServicer_to_server(Echo(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print(f'Server: started on port {port}')
    return server

def stop_server():
    print("Server: Stopping.")
    server.stop(0)
    print("Server: Stopped.  Exiting...")
    sys.exit(0)

def signal_handler(signum, frame):
    stop_server()


server = None;

if __name__ == '__main__':
    # start the server
    server = start_server()

    # catch ctrl+c and kill signals so we exit gracefully
    signal.signal(signal.SIGINT, signal_handler)  # ctrl+c
    signal.signal(signal.SIGTERM, signal_handler) # kill / Terminate

    # keep the server running until interrupted
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        stop_server()