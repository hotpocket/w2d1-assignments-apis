# Using grpc
Use grpc to conduct communications between a client and server that we are to write.

## Summary
The service I chose to create is a simple echo service that  echo's the string passed to the server, back to the client.

This is done via an api spec written in the protocol buffers syntax. The file where the API is defined is `echo.proto`.  Python is generated from this proto file that defines the classes that enforce the API call constraints. There are two files: `client.py` and `server.py`, that use the generated python to  conduct the message passing as per the API spec.

## Project Structure
* `echo.proto` - The API definition.  The core file from which all else is generated and references. We have the `EchoMessage` service, and a defination on how to define the request and response via the `EchoRequest` , and `EchoResponse` blocks
* `init_env` - Ment to be sourced into your environment.  Will create the virtual environment, generate the python stubs, start the server, run the tests, and tear down deactiveate the virtual environment.  It will leave the stub files and generated stuff... There is no cleanup script.
* `gen_proto.sh` - Will generate the protocol buffer python files that implement the API defined in `echo.proto`
* `server.py` - The server that accepts `message`s via the above specs in the above service.  Makes use of classes generated via `gen_proto.sh`
* `client.py` - The client that sends `message`s via the specs and service mentioned above. Makes use of classes generated via `gen_proto.sh`



## Challenges
This assignment presented significant challenges.  It's easy to copy a piece of code off the internet and run it.  It's another thing entirely to understand the flow of information taking place and the stack that controls this flow.

Getting a handle on the complexity of this task was challenging.  There was termonology, technology, history, and impementation specific details that encapsulate concepts that were hurdles to overcome.  I was familar with what a protocol was and the OSI model, but I would imagine not having this knowledge would present additional hurdles, if one did not have it.

I chose to use python and had to get a handle on what files were generated, and how they were to interact with the client and server files I was to write.  Furthermore what needed to be contained in these files and how to organize it took some time.

To wrangle this complexity I created several scripts to: generate the python stubs (`gen_proto.sh`), initalize the environment (`init_env`), and run tests (`run_tests.sh`).

## Things learned
Everything.  I had never heard of grpc or protocol buffers before.  The reason for their existence is easy to understand, as there are many many protocols out there that have a focus on efficient communication (rsync, wbxml, etc...).  It was frustrating but rewarding.  No mud no lotus.

