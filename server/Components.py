import logging

components = {}


def register(name, component):
    components[name] = component

def getComponent(name):
    return components[name];

def run():
    componentsStart()
    componentsUpdate()

def componentsStart():
    logging.info("Starting components")
    for component in components.values():
        component.start()


def componentsUpdate():
    logging.info("Entering component loop")
    while True:
        for component in components.values():
            component.update()
