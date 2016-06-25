import logging

from server.Comunication import Comunication
from server.Fibonachi import Fibonachi
from server.MotorControler import MotorControler


class ComponentCreator():
    def __init__(self):
        self.createComponents()

    def createComponents(self):
        logging.info("Creating components")
        MotorControler("MotorControler")
        Comunication("Comunication")
