from enum import Enum

from server.Component import Component


class MovementState(Enum):
    forward = 0
    backward = 1
    left = 2
    right = 3
    stop = 4


class MotorControler(Component):
    state = MovementState.stop

    def destroy(self):
        pass

    def update(self):
        print(self.state)

    def start(self):
        pass
