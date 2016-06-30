import logging
from .Comunication import Comunication
from .Fibonachi import Fibonachi
from .MotorControler import MotorControler


class ComponentCreator:
    def __init__(self):
        self.createComponents()

    def createComponents(self):
        logging.info("Creating components")
        MotorControler("MotorControler")
        Comunication("Comunication")
