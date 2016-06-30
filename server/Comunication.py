import threading

from server import Components
from server.Component import Component
import socketserver

from .MotorControler import MovementState


class Comunication(Component):
    def destroy(self):
        pass

    def update(self):
        pass

    def start(self):
        thread = comunicationThread()
        thread.start()


class comunicationThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("Starting to listen")
        HOST, PORT = "localhost", 9999
        server = socketserver.TCPServer((HOST, PORT), ComunicationTCPHandler)
        server.serve_forever()


class ComunicationTCPHandler(socketserver.BaseRequestHandler):
    from server.MotorControler import MovementState
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        self.data = self.data.decode("utf-8")
        motorControler = Components.getComponent("MotorControler")
        if self.data == "Forward":
            motorControler.state = MovementState.forward
        elif self.data == "Backward":
            motorControler.state = MovementState.backward
        elif self.data == "Left":
            motorControler.state = MovementState.left
        elif self.data == "Right":
            motorControler.state = MovementState.right
        elif self.data == "Stop":
            motorControler.state = MovementState.stop
