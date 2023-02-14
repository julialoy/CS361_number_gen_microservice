# CS361 Number Generator Microservice
A microservice that provides 3 unique pseudorandom numbers to a client upon request. Requires [Python]("https://www.python.org/downloads/") and [PyZMQ]("https://github.com/zeromq/pyzmq#building-and-installation") to run.   

---
### Server Overview: Data as JSON
The file server_json_example.py implements the microservice described above and returns all data as a JSON object. Any client connecting to server.py should expect all data received to be a valid JSON object and must send data as a **bytes-like object/sequence of bytes**. The client is responsible for decoding data sent by the server and manipulating it as needed.


#### Installation and running:
1. Ensure you have a valid version of Python installed. [Python v. 3.11.0]("https://www.python.org/downloads/") is recommended. A Python version >= v. 3.4 is required.
2. Ensure you have [PyZmQ]("https://github.com/zeromq/pyzmq#building-and-installation") installed.
3. Download server_json_example.py.
4. Start server_json_example.py:  
    ```python 
    python server_json_example.py
    ```
5. Server is now ready to receive client connections.  

---

### Requesting Data
The server opens a socket via TCP on localhost on port 5555. To request data from the server:
1. A client program should first create a socket and establish a connection to tcp://localhost:5555. Example using PyZMQ's socket API:   
    ```python
    s = context.socket(zmq.REQ)
    s.connect("tcp://localhost:5555")
    ```
2. Once the connection is established, the client program must send a message to the server indicating the client is requesting information. The message may be any string other than "q", encoded as a sequence of bytes. Below is an example using PyZMQ's socket API:   
   ```python
   msg = "ready"
   s.send(msg.encode())
   ```   
---

### Receiving Data
A client program will receive data from the server via the socket connection described above in **Requesting Data**. Data received will be a JSON object. Below is an example using PyZMQ's socket API:  
   ```python
   data_recvd = client_sock.recv_json()
   ```

---  
### UML Diagram  
![]("https://github.com/julialoy/CS361_number_gen_microservice/blob/master/UML.jpg?raw=true")
---  
### Additional Notes:
  * The server's default port is 5555. If a different port is needed, open the server_json_example.py file and change the PORT variable at the top of the file.
  * To facilitate testing and troubleshooting, the server will terminate the connection and shut down if it receives the data ```b'q'``` (i.e., "q" encoded as a sequence of bytes) from the client. This can be disabled by commenting out the relevant code in server_json_example.py. The bit of code to comment out is clearly delimited by a comment header.
