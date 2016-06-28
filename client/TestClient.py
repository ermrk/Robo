#!/usr/bin/python           # This is client.py file

import socket  # Import socket module

while True:
    direction = input("Where do you want to go?")
    s = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    port = 9999  # Reserve a port for your service.
    s.connect(("localhost", port))
    s.send(direction.encode("utf-8"))
    received = s.recv(1024)
    s.close  # Close the socket when done
