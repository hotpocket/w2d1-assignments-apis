import grpc
import echo_pb2
import echo_pb2_grpc

def run():
  message="hello"
  print(f'Client: Sending "{message}" to server.')
  with grpc.insecure_channel('localhost:50051') as channel:
    stub = echo_pb2_grpc.EchoStub(channel)
    response = stub.EchoMessage(echo_pb2.EchoRequest(message=message))
    print(f'Client: received "{response.message}" from server.')

if __name__ == '__main__':
  run()
